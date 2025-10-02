const input = $input.first()?.json ?? {};
const abteilung = input.abteilung || {};
const position = input.position ?? 0;

const globalData = $getWorkflowStaticData('global');
const context = globalData.context || {};
const availableProcesses = Array.isArray(globalData.availableProcesses) ? globalData.availableProcesses : [];

const limitProcesses = (processes, limit = 120) => {
  if (processes.length <= limit) return processes;
  return processes.slice(0, limit);
};

const prozessPool = limitProcesses(availableProcesses);
const rollenGesamt = Array.isArray(context.rollen) ? context.rollen : [];
const rollen = rollenGesamt.filter(rolle => rolle.abteilung_id === abteilung.id).slice(0, 10);

const unternehmen = context.unternehmen || {};
const config = context.config || {};

// DEBUG: Prüfe ob Prozesse verfügbar sind
console.log('=== ABTEILUNGSKONTEXT DEBUG ===');
console.log('Abteilung:', abteilung.name);
console.log('Available processes:', availableProcesses.length);
console.log('Process pool:', prozessPool.length);
if (prozessPool.length > 0) {
  console.log('First 3 processes:', prozessPool.slice(0, 3).map(p => ({ pcf_id: p.pcf_id, name: p.name })));
}

// Wenn keine Prozesse verfügbar, überspringe
if (prozessPool.length === 0) {
  console.log('WARNUNG: Keine Prozesse verfügbar!');
  return [{ json: {
    abteilung,
    rollen,
    prozessPool: [],
    config,
    position,
    requestPayload: null,
    skipReason: 'no_processes_available'
  }}];
}

// Erstelle konkrete Beispiele aus den tatsächlich verfügbaren Prozessen
const beispielProzesse = prozessPool.slice(0, 3).map(p =>
  'pcf_id: "' + p.pcf_id + '", hierarchy_id: "' + p.hierarchy_id + '"'
).join(' | ');

const systemPrompt = 'Du bist Organisations- und Prozessberater. Wähle für die Abteilung 1-2 passende APQC Level-3-Prozesse aus der bereitgestellten Liste.\n\n' +
  'KRITISCH - Du MUSST die Prozess-IDs EXAKT aus der verfügbaren Liste kopieren:\n' +
  '1. Suche in der "Verfügbare APQC-Prozesse Level 3" Liste nach passenden Prozessen\n' +
  '2. Kopiere die pcf_id EXAKT aus der Liste (z.B. ' + beispielProzesse + ') - KEINE eigenen IDs erfinden!\n' +
  '3. Kopiere die hierarchy_id EXAKT aus der Liste - KEINE eigenen IDs erfinden!\n' +
  '4. Kopiere name und description EXAKT - Wort für Wort wie in der Liste!\n' +
  '5. Wähle 1-2 Prozesse (bis zu 4 wenn Abteilung sehr komplex)\n' +
  '6. NIEMALS eigene Prozesse erfinden - NUR aus der verfügbaren Liste wählen!\n\n' +
  'Die Liste enthält ' + prozessPool.length + ' verfügbare Prozesse. Wähle NUR Prozesse aus dieser Liste!';

const abteilungsInfo = {
  id: abteilung.id,
  name: abteilung.name,
  ebene: abteilung.ebene,
  mitarbeiter: abteilung.mitarbeiteranzahl,
};

const rollenInfo = rollen.map(rolle => ({
  id: rolle.id,
  titel: rolle.titel,
  ebene: rolle.ebene,
}));

const unternehmensInfo = {
  name: unternehmen.name,
  branche: unternehmen.branche,
  mitarbeiteranzahl: unternehmen.mitarbeiteranzahl,
  besonderheit: config.besonderheit || null,
};

const userSections = [
  'Unternehmenskontext:',
  JSON.stringify(unternehmensInfo, null, 2),
  '',
  'Abteilung:',
  JSON.stringify(abteilungsInfo, null, 2),
  '',
  'Rollen in dieser Abteilung (Auszug):',
  JSON.stringify(rollenInfo, null, 2),
  '',
  'Verfügbare APQC-Prozesse Level 3:',
  JSON.stringify(prozessPool, null, 2),
  '',
  'Aufgabe:',
  'Wähle 1-2 Prozesse aus (mehr nur wenn die Abteilung sehr komplex ist). Die Felder pcf_id, hierarchy_id, name und description müssen EXAKT aus der Liste übernommen werden. Gib zusätzlich eine kurze Begründung (warum passt dieser Prozess) und Priorität (hoch/mittel/niedrig) an. Setze abteilung_id auf "' + abteilung.id + '" und abteilung_name auf "' + abteilung.name + '".',
];

const requestPayload = {
  model: 'gpt-4o-mini',
  temperature: 0.1,
  response_format: {
    type: 'json_schema',
    json_schema: {
      name: 'prozesse_response',
      schema: {
        type: 'object',
        additionalProperties: false,
        properties: {
          prozesse: {
            type: 'array',
            minItems: 1,
            maxItems: 4,
            items: {
              type: 'object',
              additionalProperties: false,
              properties: {
                pcf_id: { type: 'string' },
                hierarchy_id: { type: 'string' },
                name: { type: 'string' },
                description: { type: 'string' },
                abteilung_id: { type: 'string' },
                abteilung_name: { type: 'string' },
                begruendung: { type: 'string' },
                prioritaet: { type: 'string', enum: ['hoch', 'mittel', 'niedrig'] },
              },
              required: ['pcf_id', 'hierarchy_id', 'name', 'description', 'abteilung_id', 'abteilung_name'],
            },
          },
        },
        required: ['prozesse'],
      },
    },
  },
  messages: [
    { role: 'system', content: systemPrompt },
    { role: 'user', content: userSections.join('\n') },
  ],
};

console.log('Request payload created, message length:', JSON.stringify(requestPayload).length);

return [
  {
    json: {
      unternehmen,
      abteilung,
      rollen,
      prozessPool,
      config,
      position,
      requestPayload,
    },
  },
];
