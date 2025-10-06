const config = $input.first().json;

if (config.use_demo_data) {
  const unternehmen = {
    id: '12345678',
    name: 'Dolce Gelato GmbH',
    branche: 'Lebensmittel & Gastronomie',
    groesse: 'Mittel',
    mitarbeiteranzahl: 150,
    gruendungsjahr: 2010,
    hauptsitz: 'München, Deutschland',
    beschreibung: 'Dolce Gelato GmbH stellt handgemachtes Eis aus regionalen und biologischen Zutaten her und betreibt mehrere Filialen in Süddeutschland.',
    umsatz_mio: 12,
    webseite: 'www.dolcegelato.de'
  };

  const abteilungen = [
    { id: 'dept_001', unternehmen_id: '12345678', name: 'Geschäftsführung', ebene: 1, parent_id: null, beschreibung: 'Strategische Leitung', mitarbeiteranzahl: 3 },
    { id: 'dept_002', unternehmen_id: '12345678', name: 'Produktion', ebene: 2, parent_id: 'dept_001', beschreibung: 'Eisherstellung und Qualitätskontrolle', mitarbeiteranzahl: 45 },
    { id: 'dept_003', unternehmen_id: '12345678', name: 'Vertrieb & Filialen', ebene: 2, parent_id: 'dept_001', beschreibung: 'Verkauf und Kundenservice', mitarbeiteranzahl: 102 }
  ];

  const rollen = [
    { id: 'role_001', abteilung_id: 'dept_001', titel: 'Geschäftsführer', beschreibung: 'Strategische Unternehmensführung', ebene: 'Executive', anzahl_personen: 1, gehalt_min: 90000, gehalt_max: 120000, anforderungen: ['Führungserfahrung', 'Strategisches Denken', 'Kenntnisse Lebensmittelbranche'] },
    { id: 'role_002', abteilung_id: 'dept_002', titel: 'Produktionsleiter Eiscreme', beschreibung: 'Leitung der Eisproduktion', ebene: 'Lead', anzahl_personen: 1, gehalt_min: 55000, gehalt_max: 70000, anforderungen: ['Lebensmitteltechnik', 'Qualitätskontrolle', 'Teamführung'] },
    { id: 'role_003', abteilung_id: 'dept_003', titel: 'Filialleiter', beschreibung: 'Leitung einer Eisdiele-Filiale', ebene: 'Mid', anzahl_personen: 1, gehalt_min: 38000, gehalt_max: 48000, anforderungen: ['Kundenservice', 'Verkaufserfahrung'] }
  ];

  const mitarbeiter = [
    { id: 'emp_001', rolle_id: 'role_001', abteilung_id: 'dept_001', vorname: 'Isabella', nachname: 'Rossi', email: 'i.rossi@dolcegelato.de', telefon: '+49 89 1234567', alter: 42, geschlecht: 'weiblich', motivation: 'hoch', intelligenz: 'hoch', gehalt_euro: 105000, eintrittsdatum: '2010-03-15', vertrag: 'Vollzeit', standort: 'München, Deutschland', unternehmen_id: '12345678', vollname: 'Isabella Rossi' },
    { id: 'emp_002', rolle_id: 'role_002', abteilung_id: 'dept_002', vorname: 'Marco', nachname: 'Bianchi', email: 'm.bianchi@dolcegelato.de', telefon: '+49 89 2345678', alter: 35, geschlecht: 'männlich', motivation: 'hoch', intelligenz: 'mittel', gehalt_euro: 62000, eintrittsdatum: '2015-06-01', vertrag: 'Vollzeit', standort: 'München, Deutschland', unternehmen_id: '12345678', vollname: 'Marco Bianchi' },
    { id: 'emp_003', rolle_id: 'role_003', abteilung_id: 'dept_003', vorname: 'Sofia', nachname: 'Ferrari', email: 's.ferrari@dolcegelato.de', telefon: '+49 89 3456789', alter: 28, geschlecht: 'weiblich', motivation: 'mittel', intelligenz: 'mittel', gehalt_euro: 43000, eintrittsdatum: '2019-09-15', vertrag: 'Vollzeit', standort: 'München, Deutschland', unternehmen_id: '12345678', vollname: 'Sofia Ferrari' }
  ];

  const prozesse = [
    {
      id: 'proc_001',
      pcf_id: '10551',
      hierarchy_id: '4.2.1',
      name: 'Rohstoffe und Materialien beschaffen',
      description: 'Beschaffung von Rohmaterialien für die Produktion.',
      spezifischer_name: 'Beschaffung regionaler Bio-Zutaten für Eis',
      abteilung_id: 'dept_002',
      abteilung_name: 'Produktion',
      begruendung: 'Hochwertige regionale Zutaten sind essentiell für die Qualität unseres handgemachten Eises.',
      prioritaet: 'hoch'
    },
    {
      id: 'proc_002',
      pcf_id: '10607',
      hierarchy_id: '4.3.1',
      name: 'Produktionsaufträge planen und terminieren',
      description: 'Planung und Zeitplanung der Produktionsaufträge.',
      spezifischer_name: 'Produktionsplanung für saisonale Eissorten',
      abteilung_id: 'dept_002',
      abteilung_name: 'Produktion',
      begruendung: 'Effiziente Planung sichert frische Eis-Produktion entsprechend der saisonalen Nachfrage.',
      prioritaet: 'hoch'
    },
    {
      id: 'proc_003',
      pcf_id: '10770',
      hierarchy_id: '5.1.1',
      name: 'Kundenservicestrategien entwickeln',
      description: 'Entwicklung von Strategien für exzellenten Kundenservice.',
      spezifischer_name: 'Service-Konzept für Eisdiele-Filialen',
      abteilung_id: 'dept_003',
      abteilung_name: 'Vertrieb & Filialen',
      begruendung: 'Erstklassiger Service in unseren Filialen ist entscheidend für Kundenzufriedenheit und Wiederkauf.',
      prioritaet: 'hoch'
    }
  ];

  return [{ json: { unternehmen, abteilungen, rollen, mitarbeiter, prozesse, config } }];
} else {
  return [];
}
