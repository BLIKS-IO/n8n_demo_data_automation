#!/usr/bin/env python3
import json
import sys

# Neue Prozesse-Daten
neue_prozesse = [
    { 'pcf_id': '10017', 'hierarchy_id': '1.1.1', 'name': 'Bewertung der externen Umgebung', 'description': 'Die Bewertung aller Kräfte, Entitäten und Systeme, die außerhalb einer Organisation liegen, aber deren Betrieb beeinflussen können. Die Analyse weitreichender Strömungen in der makroökonomischen Situation, die Bewertung des Wettbewerbs, die Beurteilung technologischer Veränderungen und die Identifizierung gesellschaftlicher sowie ökologischer Anliegen. Ein umfassendes Verständnis der Externalitäten schaffen, mit ausreichender Tiefe in den einzelnen Aspekten.', 'spezifischer_name': 'Analyse der externen Technologie-Umgebung', 'abteilung_id': 'dept_001', 'abteilung_name': 'Geschäftsführung', 'begruendung': 'Die Geschäftsführung muss die externen Faktoren, die die Technologiebranche beeinflussen, kontinuierlich bewerten, um strategische Entscheidungen zu treffen.', 'prioritaet': 'hoch' },
    { 'pcf_id': '10020', 'hierarchy_id': '1.1.4', 'name': 'Eine strategische Vision entwickeln', 'description': 'Die langfristige Vision der Organisation als strategische Positionierung und Einbindung der Interessengruppen etablieren. Die Vision durch die Schaffung strategischer Ausrichtungen aller Interessengruppen umsetzen. Die Rahmenwerke zur Strategieentwicklung in diesem Kontext verstehen.', 'spezifischer_name': 'Entwicklung einer nachhaltigen Technologie-Vision', 'abteilung_id': 'dept_001', 'abteilung_name': 'Geschäftsführung', 'begruendung': 'Die Geschäftsführung benötigt eine klare Vision, um die nachhaltigen Ziele des Unternehmens in der Technologiebranche zu definieren und zu kommunizieren.', 'prioritaet': 'hoch' },
    { 'pcf_id': '10039', 'hierarchy_id': '1.2.3', 'name': 'Langfristige Unternehmensstrategie entwickeln.', 'description': 'Entwicklung einer Strategie zur Erreichung der Unternehmensziele in ferner Zukunft. Eine der strategischen Optionen zur langfristigen Verwirklichung der Mission annehmen. Einbeziehung von Führungskräften des oberen Managements, bestehend aus Strategie- und/oder Geschäftseinheitspersonal.', 'spezifischer_name': 'Langfristige Strategie für nachhaltige Technologien', 'abteilung_id': 'dept_001', 'abteilung_name': 'Geschäftsführung', 'begruendung': 'Die Entwicklung einer langfristigen Strategie ist entscheidend, um die nachhaltigen Lösungen des Unternehmens im Technologiemarkt zu fördern.', 'prioritaet': 'hoch' },
    { 'pcf_id': '10061', 'hierarchy_id': '2.1.1', 'name': 'Entwicklung strategischer Initiativen', 'description': 'Entwicklung strategischer Projekte, die zur Erreichung langfristiger Ziele beitragen. Entwicklung zeitlich begrenzter Projekte, die freiwilliger Natur sind und über den Rahmen der routinemäßigen Abläufe der Organisation hinausgehen.', 'spezifischer_name': 'Strategische Initiativen für nachhaltige Technologien', 'abteilung_id': 'dept_001', 'abteilung_name': 'Geschäftsführung', 'begruendung': 'Die Geschäftsführung muss strategische Initiativen entwickeln, um innovative und nachhaltige Lösungen in der Technologiebranche voranzutreiben.', 'prioritaet': 'mittel' },
    { 'pcf_id': '10018', 'hierarchy_id': '1.1.2', 'name': 'Untersuchen des Marktes und Ermitteln der Bedürfnisse und Wünsche der Kunden.', 'description': 'Den Markt untersuchen, um kundenorientierte Lösungen zu identifizieren. Die relevanten Märkte bewerten, um die Produkte/Dienstleistungen zu bestimmen, die von Kunden benötigt oder gewünscht werden. Quantitative und qualitative Analysen durchführen, um Produkte/Dienstleistungen zu erfassen und zu untersuchen. Kreative Techniken einsetzen, die ein besseres Verständnis des Kunden ermöglichen und relevante Lösungen entwerfen.', 'spezifischer_name': 'Marktforschung für nachhaltige Technologien', 'abteilung_id': 'dept_003', 'abteilung_name': 'Produktentwicklung', 'begruendung': 'Die Produktentwicklung erfordert ein tiefes Verständnis der Marktbedürfnisse, um innovative und nachhaltige Lösungen zu schaffen.', 'prioritaet': 'hoch' },
    { 'pcf_id': '10037', 'hierarchy_id': '1.2.1', 'name': 'Entwickeln einer übergreifenden Missionserklärung', 'description': 'Einen übergreifenden, kompakten Satz formulieren, der die Mission der Organisation prägnant unterstreicht. Eine klare und prägnante Missionserklärung definieren und kommunizieren, die zusammenfasst, wie die Organisation vorgehen möchte, um eine strategische Vision zu entwickeln. Kritische Beiträge von der Geschäftsleitung und Strategieexperten einholen und mit dem Marketing oder Mitarbeitern aus verwandten Funktionen zusammenarbeiten.', 'spezifischer_name': 'Mission für nachhaltige Produktentwicklung', 'abteilung_id': 'dept_003', 'abteilung_name': 'Produktentwicklung', 'begruendung': 'Eine klare Mission ist entscheidend, um die Richtung der Produktentwicklung im Bereich nachhaltiger Technologien zu steuern.', 'prioritaet': 'hoch' },
    { 'pcf_id': '10065', 'hierarchy_id': '2.2.1', 'name': 'Führe Entdeckungsforschung durch.', 'description': 'Koordinierung der F&E-Aktivitäten zur Identifizierung neuer Technologien, die in das überarbeitete Produkt-/Dienstleistungsportfolio integriert werden können. Durchführung von F&E-Aktivitäten in der Frühphase, um Lücken zwischen bestehenden Lösungsangeboten und sich ändernden Markterwartungen zu schließen. Triangulation geeigneter Technologien, die die Entwicklung eines überarbeiteten Produkt-/Dienstleistungsportfolios unterstützen können.', 'spezifischer_name': 'Forschung für innovative nachhaltige Lösungen', 'abteilung_id': 'dept_003', 'abteilung_name': 'Produktentwicklung', 'begruendung': 'Die Identifizierung neuer Technologien ist entscheidend für die Entwicklung innovativer, nachhaltiger Produkte.', 'prioritaet': 'hoch' },
    { 'pcf_id': '19990', 'hierarchy_id': '2.2.3', 'name': 'Produkt-/Dienstentwicklungsanforderungen definieren', 'description': 'Umfasst die Identifizierung und Erfassung neuer Produkt-/Dienstleistungsanforderungen oder potenzieller Verbesserungen bestehender Produkte/Dienstleistungen. Zusammenarbeit mit Mitgliedern der Lieferkette, um die Machbarkeit der in den Anforderungen definierten Punkte sicherzustellen. Ein Beispiel wäre ein Produkt mit Herstellungsanforderungen, die die Lieferkette derzeit nicht erfüllen kann, was eine unternehmerische Entscheidung erfordert, entweder die Fertigungskapazitäten zu erweitern oder das neue Produkt aufzugeben. Auswirkungen und Bedürfnisse auf Unternehmensebene müssen berücksichtigt werden. Abhängig von der Art des Endprodukts oder der Dienstleistung werden diese Anforderungen oft als eine Reihe von Fähigkeiten definiert, wie Verfügbarkeit oder Zuverlässigkeit, die die Entscheidungen zur Produktentwicklung beeinflussen.', 'spezifischer_name': 'Anforderungen für nachhaltige Produktentwicklung definieren', 'abteilung_id': 'dept_003', 'abteilung_name': 'Produktentwicklung', 'begruendung': 'Die Definition von Anforderungen ist entscheidend, um sicherzustellen, dass neue Produkte den Nachhaltigkeitsstandards entsprechen.', 'prioritaet': 'hoch' },
    { 'pcf_id': '10106', 'hierarchy_id': '3.1.1', 'name': 'Kunden- und Marktanalysen durchführen', 'description': 'Informationen über den Markt und die Kunden sammeln. Die inhärenten Eigenschaften und das kollektive Verhalten der verschiedenen Markt- und Kundensegmente genau untersuchen. Trends im Markt verfolgen. Herausfinden, was die Kunden zu Kaufentscheidungen bewegt, um Chancen im Markt zu identifizieren.', 'spezifischer_name': 'Marktforschung für nachhaltige Technologien', 'abteilung_id': 'dept_002', 'abteilung_name': 'Vertrieb & Marketing', 'begruendung': 'Die Analyse von Kunden und Markttrends ist entscheidend, um die Bedürfnisse der Zielgruppe im Bereich nachhaltiger Technologien zu verstehen und passende Lösungen anzubieten.', 'prioritaet': 'hoch' },
    { 'pcf_id': '10107', 'hierarchy_id': '3.1.2', 'name': 'Bewerten und priorisieren von Marktchancen', 'description': 'Bewertung von Marktchancen durch Quantifizierung und Priorisierung sowie Validierungstests. Eine genaue Untersuchung der identifizierten Marktchancen durch die Durchführung von Kunden- und Marktanalysen [10106]. Diese Chancen werden durch die Suche nach einer Übereinstimmung zwischen den identifizierten Möglichkeiten und dem Zusammenspiel von organisatorischen Fähigkeiten und Geschäftsstrategie genutzt.', 'spezifischer_name': 'Priorisierung von Marktchancen für grüne Technologien', 'abteilung_id': 'dept_002', 'abteilung_name': 'Vertrieb & Marketing', 'begruendung': 'Die Priorisierung von Marktchancen hilft, die Ressourcen effizient zu nutzen und die vielversprechendsten Möglichkeiten im Bereich nachhaltiger Technologien zu identifizieren.', 'prioritaet': 'hoch' },
    { 'pcf_id': '10040', 'hierarchy_id': '1.2.4', 'name': 'Koordinieren und Abstimmen von bereichsübergreifenden und prozessbezogenen Strategien', 'description': 'Den Ansatz und die Methode der einzelnen Einheiten, Abteilungen, Systeme und Abläufe innerhalb der Organisation in Übereinstimmung mit dem größeren strategischen Kurs ausrichten. Den strategischen Weg der Organisation nutzen, um die Funktionen, Abteilungen und Abläufe zu leiten. Den Plan und die Methode jedes Funktionsbereichs sowie die darin enthaltenen Prozesse kalibrieren, um die langfristige Geschäftsstrategie auszuwählen [10039].', 'spezifischer_name': 'Strategische Abstimmung für nachhaltige Lösungen', 'abteilung_id': 'dept_002', 'abteilung_name': 'Vertrieb & Marketing', 'begruendung': 'Die Abstimmung der Strategien ist wichtig, um sicherzustellen, dass alle Abteilungen auf die gemeinsamen Ziele im Bereich nachhaltiger Technologien hinarbeiten.', 'prioritaet': 'mittel' },
    { 'pcf_id': '10149', 'hierarchy_id': '3.3.2', 'name': 'Marketingbudgets festlegen', 'description': 'Erstellen eines Budgets für die Marketingbemühungen der Organisation, das im Einklang mit der unternehmensweiten strategischen Ausrichtung steht. Entwickeln eines Plans zur Verteilung der Ressourcen, um die Marketingstrategie im Hinblick auf die Gesamtgeschäftsstrategie zu erreichen. Kostenannahmen treffen; das geschätzte Gesamteinkommen aus den Marketingaktivitäten im Vergleich zu den Kosten/Ausgaben dieser Aktivitäten berechnen. Die Kapitalrendite prognostizieren. Kosten den entsprechenden Marketingaktivitäten wie Werbekampagnen, Werbung, Marketingkommunikation, PR-Kampagnen, Personal und Büroräume zuordnen. Die Finanz- und Marketingfunktionen einbeziehen.', 'spezifischer_name': 'Budgetierung für nachhaltige Marketingstrategien', 'abteilung_id': 'dept_002', 'abteilung_name': 'Vertrieb & Marketing', 'begruendung': 'Ein effektives Budget ist entscheidend, um die Marketingaktivitäten für nachhaltige Lösungen effizient zu planen und die Ressourcen optimal zu nutzen.', 'prioritaet': 'hoch' }
]

# Datei laden
with open('/Users/maltepfeiffer/Documents/Code/Bliks/n8n_demo_data_automation/Unternehmensstruktur Generator mit LLM v43.json', 'r', encoding='utf-8') as f:
    workflow = json.load(f)

# AUFGABE 1: Demo-Daten Prozesse aktualisieren
for node in workflow['nodes']:
    if node['id'] == '634257ec-962f-47f4-990c-b615de13a6ec':  # Demo-Daten (Alle)
        # JavaScript-Code aus dem Node extrahieren
        js_code = node['parameters']['jsCode']

        # Alten Prozesse-Code finden und ersetzen
        # Wir müssen den alten Array-Teil finden und ersetzen
        import re

        # Prozesse-Array als JavaScript-String formatieren
        prozesse_js = json.dumps(neue_prozesse, ensure_ascii=False, indent=4)
        # Ersetze JSON-Format durch JavaScript-Format (ohne Anführungszeichen um Keys)
        prozesse_js = prozesse_js.replace('"pcf_id":', 'pcf_id:')
        prozesse_js = prozesse_js.replace('"hierarchy_id":', 'hierarchy_id:')
        prozesse_js = prozesse_js.replace('"name":', 'name:')
        prozesse_js = prozesse_js.replace('"description":', 'description:')
        prozesse_js = prozesse_js.replace('"spezifischer_name":', 'spezifischer_name:')
        prozesse_js = prozesse_js.replace('"abteilung_id":', 'abteilung_id:')
        prozesse_js = prozesse_js.replace('"abteilung_name":', 'abteilung_name:')
        prozesse_js = prozesse_js.replace('"begruendung":', 'begruendung:')
        prozesse_js = prozesse_js.replace('"prioritaet":', 'prioritaet:')

        # Pattern zum Finden des Prozesse-Arrays
        pattern = r'const prozesse = \[[\s\S]*?\];'
        replacement = f'const prozesse = {prozesse_js};'

        # Code aktualisieren
        updated_code = re.sub(pattern, replacement, js_code)
        node['parameters']['jsCode'] = updated_code

        print("✓ AUFGABE 1 abgeschlossen: Demo-Prozesse aktualisiert")
        break

# AUFGABE 2: Skip-Logik zu "Prozessiteration vorbereiten" hinzufügen
for node in workflow['nodes']:
    if node['id'] == 'f030fe13-b3a9-4aaf-843b-b3abb0e642be':  # Prozessiteration vorbereiten
        js_code = node['parameters']['jsCode']

        # Skip-Logik am Anfang hinzufügen
        skip_logic = """const input = $input.first()?.json ?? {};
const config = input.config || {};

// Wenn Demo-Prozesse verwendet werden sollen, überspringe die Iteration
if (config.use_demo_prozesse) {
  console.log('=== PROZESSITERATION ÜBERSPRUNGEN (Demo-Prozesse) ===');
  // Gebe leeres Array zurück um Loop zu überspringen
  return [];
}

"""

        # Prüfen ob Skip-Logik bereits vorhanden ist
        if 'use_demo_prozesse' not in js_code:
            # Ersetze die erste Zeile mit der neuen Skip-Logik + alte erste Zeile
            lines = js_code.split('\n')
            # Entferne die ersten zwei Zeilen (const input = ... und const { ... )
            # und füge stattdessen die Skip-Logik ein

            # Finde wo der Destrukturing-Block endet
            destruktur_end = js_code.find('} = input;')
            if destruktur_end != -1:
                # Extrahiere den Teil nach dem Destrukturing
                after_destruktur = js_code[destruktur_end + len('} = input;'):].lstrip('\n')

                # Baue neuen Code zusammen
                updated_code = skip_logic + 'const {\n  unternehmen = {},\n  abteilungen = [],\n  rollen = [],\n  apqcProcesses = [],\n  apqcActivities = [],\n  apqcActivitiesByProcess = {},\n  config = {},\n} = input;\n' + after_destruktur

                node['parameters']['jsCode'] = updated_code
                print("✓ AUFGABE 2 abgeschlossen: Skip-Logik hinzugefügt")
        else:
            print("⚠ AUFGABE 2: Skip-Logik bereits vorhanden")
        break

# Datei speichern
with open('/Users/maltepfeiffer/Documents/Code/Bliks/n8n_demo_data_automation/Unternehmensstruktur Generator mit LLM v43.json', 'w', encoding='utf-8') as f:
    json.dump(workflow, f, ensure_ascii=False, indent=2)

print("\n✅ Workflow erfolgreich aktualisiert!")
