# Personal AI Workshop

**Deutsch** · [English](README.en.md)

**Ein Einstieg. Viele Pakete. Erfahrung, die bleibt.**

[Interaktive Agentenrunde öffnen](https://markusschwarz174.github.io/personal-ai-workshop/)

## Warum versteht mich GPT nicht?

Das ist die Frage, die ich mir oft stelle, wenn ich mit einem neuen Chat etwas bauen will. Ich habe alles detailliert im Kopf und beschreibe es im Prompt. Trotzdem kann ich nie sicher sein, wie sich eine Session entwickeln wird. Es ist, als würden GPT und ich unterschiedliche Sprachen sprechen.

Beim Nachdenken über dieses Problem kommen mir zwei Zahnräder in den Sinn, die ineinandergreifen müssen: die Synchronisation von HUMAN und Maschine.

Aus dieser Idee entsteht der `STARTER_AGENT`, kurzzeitig `AUSRICHTER` genannt. Er soll vor der eigentlichen Arbeit einige Dinge klären: Was ist der Auftrag? Woran erkennen wir Erfolg? Was gehört dazu – und was nicht? Welche Quellen gelten? Wann brechen wir ab? Und wann ist das Ergebnis gut genug? Am Ende soll ein Master-Prompt stehen, der HUMAN und Maschine aufeinander ausrichtet.

Ich setze diesen Entwurf nie als Pilot ein und verschiebe ihn später ins Archiv. Doch die Arbeit ist nicht umsonst. Die Vorstellung, dass es ein WELCOMING und einen einzigen Ansprechpartner braucht, bleibt. Aus den Zahnrädern wird eine Hotellobby, aus verschiedenen Namen schliesslich der `ADVISER` – mein SINGLE POINT OF CONTACT.

Über die Zeit entsteht daraus meine persönliche Runde spezialisierter Agenten. Der ADVISER empfiehlt mir nach meiner Freigabe den passenden Spezialisten, übernimmt die Übergaben und behält den Weg zum Ziel im Blick. Mit den Visualisierungsmöglichkeiten von GPT wird diese Runde nun erstmals gemeinsam und mit eigenen Gesichtern sichtbar.

[Die vollständige Entstehungsgeschichte lesen](docs/ENTSTEHUNGSGESCHICHTE.md)

## Technische Beschreibung durch KI

> **Transparenzhinweis:** Die folgende technische Beschreibung wurde durch KI nach einer Analyse der historischen MISSION CONTROL und des heutigen Agentensystems erstellt. Die persönliche Einführung und Entstehungsgeschichte stammen von Markus Schwarz.

### Was die Agentenrunde ist

Die Agentenrunde ist eine vom Menschen geführte Oberfläche für die Zusammenarbeit mit KI. Sie soll eine einfache Frage beantworten: **Wer hilft bei welcher Art von Aufgabe – und in welcher Funktion?**

Der Einstieg erfolgt über den `ADVISOR`. Er klärt das Anliegen, hält Ziel und offenen Stand zusammen und empfiehlt den kleinsten passenden Einsatz. Danach übernimmt ein Fachagent für einen klar begrenzten Arbeitsabschnitt. Der Mensch bestätigt wichtige Übergänge und behält die Entscheidungshoheit.

Der Begriff *Agent* wird hier bewusst praktisch verwendet. Er bezeichnet ein wiedererkennbares Gegenüber mit Auftrag, Haltung und Grenzen. Die Runde behauptet weder, dass sieben autonome Programme gleichzeitig arbeiten, noch dass die Visualisierung einen persistenten Systemzustand zeigt.

### Vom projektspezifischen Leitstand zur allgemeinen Agentenrunde

Der dokumentierte Vorläufer war MISSION CONTROL. Dieses Modell entstand in einem einzelnen Arbeitsworkspace als imaginärer Tisch: Der Mensch beschreibt sein Vorhaben, ein beratender Einstieg klärt Auftrag und Umfang, geeignete Rollen werden vorgeschlagen und Ergebnisse kehren zur menschlichen Entscheidung zurück. Bereits dort wurden Synchronisation, Routing, Übergaben, getrennte Arbeits- und Prüfschritte sowie das Lernen aus realen Routingfällen erprobt.

Die heutige Agentenrunde übernimmt nicht einfach alle damaligen Rollen. Sie löst sie aus dem ursprünglichen Projektkontext und ordnet die wiederverwendbaren Funktionen neu. Aus zahlreichen projektspezifischen Agenten, Helfern und Passes wurden sieben allgemein verständliche Gegenüber. Spezialisierungen werden überwiegend als **Modi** und **Kompetenzen** geführt, damit nicht für jede Tätigkeit eine neue Figur entstehen muss.

### Die sieben Agenten

| Agent | Modi | Aufgabe in einfachen Worten |
|---|---|---|
| `ADVISOR` | `SYNCHRONIZER`, `ROUTER` | Klärt das Anliegen, hält den Stand zusammen und empfiehlt den passenden Einsatz. |
| `ASSISTANT` | `RESPONDER`, `EXECUTOR` | Beantwortet einfache Fragen oder erledigt klar begrenzte Aufgaben direkt. |
| `TUTOR` | `LERNARCHITEKT`, `LERNBEGLEITER`, `WEB_RESEARCHER` | Plant und begleitet Lernen und beschafft dafür nachvollziehbare Informationen. |
| `SPARRING` | `CHALLENGER`, `SOCRATIC` | Prüft Annahmen, entwickelt Gegenpositionen und schärft das Denken durch Fragen. |
| `ARCHITECT` | `EXPLORER`, `PROPOSER`, `PLANNER`, `IMPLEMENTOR`, `DEVELOPER`, `AI_ENGINEER`, `DEBUGGER` | Untersucht, entwirft, plant, baut, verbessert und repariert technische Systeme und KI-Lösungen. |
| `GUARDIAN` | `OBSERVER`, `REVIEWER`, `VALIDATOR`, `AUDITOR` | Beobachtet, prüft und auditiert Arbeit anhand benannter Kriterien und Nachweise. `TEAM_RED` ist **Planned · not active**. |
| `TEXT_EDITOR` | `WRITER`, `READER`, `TRANSLATOR`, `VISUALIZER` | Erstellt, prüft, übersetzt und gestaltet Texte und kleinere Webauftritte. |

Pro Arbeitsabschnitt ist genau **ein Modus** aktiv. Ein Wechsel wird sichtbar gemacht. So bleibt erkennbar, ob ein Agent gerade erkundet, plant, umsetzt, prüft oder lediglich berät.

### Typischer Ablauf

```text
Idee oder Problem des Menschen
            ↓
ADVISOR klärt Ziel, Kontext und Grenzen
            ↓
Empfehlung für Agent und Modus
            ↓
menschliche Bestätigung
            ↓
klar begrenzter Arbeitsauftrag
            ↓
Facharbeit durch den zuständigen Agenten
            ↓
bei Bedarf getrennte Prüfung durch GUARDIAN
            ↓
Ergebnis zurück zu ADVISOR und Mensch
```

Vor materieller Arbeit wird der Einsatz in einem gemeinsamen Auftragsrahmen festgehalten. Dazu gehören insbesondere Aufgabe, erwartetes Ergebnis, Umfang, Eingaben, erlaubte Handlungen, Erfolgskriterien, Ausgabe sowie Abschluss- und Abbruchbedingungen. Nicht jede kleine Frage benötigt den vollständigen Ablauf: Eine einfache Antwort soll einfach bleiben.

### Technische Struktur

Die Agentenrunde ist dokumentationsbasiert und grundsätzlich providerneutral angelegt. Ihre technische Struktur besteht aus mehreren getrennten Ebenen:

- **Darstellung:** Eine interaktive Runde macht Agenten und Modi sichtbar. Sie dient der Orientierung und ist kein Live-Monitor autonomer Prozesse.
- **Identitäten:** Sieben stabile Agenten bilden die menschlich verständlichen Gegenüber.
- **Modi:** Modi beschreiben die aktuell ausgeübte Funktion eines Agenten.
- **Kompetenzen:** Fähigkeiten können agentenübergreifend verwendet werden, behalten aber eine klar bezeichnete fachliche Verantwortung.
- **Auftragsrahmen:** Ein gemeinsames Vertragsmuster bindet Ziel, Scope, erlaubte Arbeit, Erfolg und Übergabe.
- **Routing:** Eine Matrix beschreibt zulässige Zuordnungen und Übergänge zwischen Agenten, Modi und Prüfungen.
- **Validierung:** Arbeits- und Prüffunktion werden getrennt. Eine Prüfung gegen Kriterien ist etwas anderes als ein allgemeines Review oder eine Beobachtung.
- **Governance:** Es gibt eine private Regel- und Schutzebene. Sie wird in diesem Repository als vorhandene Grundlage benannt, aber nicht veröffentlicht.

Die zugrunde liegenden Arbeitsstände verwenden Markdown für lesbare Agentenprofile, YAML für Bibliothek und Zuordnungen, JSON Schema für Strukturprüfungen und HTML für die interaktive Darstellung. Die öffentliche Dokumentation beschreibt das Konzept; vollständige Agentenverträge, Systemprompts, interne Befugnisregeln und private Governance bleiben ausserhalb dieses Repositorys.

### Eigenständige Konstruktionsideen

Keine der folgenden Ideen wird als weltweite Neuerfindung beansprucht. Eigenständig ist vor allem ihre konkrete Verbindung in einem persönlichen, über längere Zeit entwickelten Arbeitssystem.

1. **Ein einziger menschlicher Einstieg ohne unsichtbare Übernahme.** Der ADVISOR bleibt ansprechbar, gibt Facharbeit aber sichtbar weiter. Er ist weder allwissender Hauptagent noch autonome Führungsebene.
2. **Wenige Identitäten, mehrere klar begrenzte Modi.** Die Runde wächst nicht für jede neue Tätigkeit um eine weitere Figur. Spezialisierung findet zuerst innerhalb einer stabilen Identität statt.
3. **Synchronisation als laufende Aufgabe.** Ziel, Entscheidungen, offener Stand und nächster Schritt werden nicht nur am Anfang geklärt, sondern während der Zusammenarbeit zusammengehalten.
4. **Schutz vor Themen-Drift.** Ein neuer Auftrag wird mit dem laufenden Arbeitsrahmen verglichen. Ein eigenständiges neues Thema wird nicht still in die bestehende Aufgabe hineingezogen.
5. **Bauen und Prüfen bleiben unterscheidbar.** Wer etwas erstellt, erklärt die eigene Kontrolle nicht automatisch zur unabhängigen Validierung. Unterschiedliche Prüfmethoden und Referenzen bilden ein Netz; es handelt sich nicht um eine Mehrheitsabstimmung zwischen Agenten.
6. **Visualisierung ohne Autonomie-Theater.** Gesichter und Tisch machen Zuständigkeiten erinnerbar. Gleichzeitig hält die technische Beschreibung fest, dass die Ansicht eine Auswahloberfläche und kein Beweis paralleler Aktivität ist.
7. **Schutz der persönlichen Stimme.** Der TEXT_EDITOR besitzt ausdrücklich die Aufgabe, starke Passagen und die Stimme des Menschen bei Kürzung, Überarbeitung und Gestaltung zu erhalten.
8. **Sichtbare Unfertigkeit.** Geplante Fähigkeiten werden nicht als aktiv dargestellt. Deshalb bleibt `TEAM_RED` ausdrücklich als **Planned · not active** gekennzeichnet.

### Verhältnis zu Version 1

Die erste Fassung dieses Repositorys beschreibt vor allem wiederverwendbare **Arbeitspakete**. Ein Paket bündelt einen vollständigen Arbeitsweg mit Rollen, Schritten, Entscheidungen, Ergebnissen, Übergaben und Validierung.

Die Agentenrunde der Version 2 ersetzt diese Idee nicht zwingend. Sie setzt früher an: Der Mensch beginnt beim ADVISOR, wählt einen passenden Agenten und kann von dort in eine einfache Direktaufgabe oder in ein umfangreicheres Arbeitspaket wechseln. Agenten beantworten damit eher die Frage **„Wer begleitet oder bearbeitet diesen Abschnitt?“**, Pakete eher die Frage **„Wie läuft dieses grössere Arbeitsstück vollständig ab?“**

Der aktuelle öffentliche Repository-Stand enthält weiterhin den paketbasierten Prototyp der ersten Fassung. Die Agentenrunde wird als zweite, parallel dokumentierte Entwicklungsstufe ergänzt. Die historischen und privaten Arbeitsstände werden dabei nicht vollständig veröffentlicht.

### Grenzen

- Die Agentenrunde garantiert keine richtigen Ergebnisse.
- Eine klare Aufgabenbeschreibung ersetzt keine fachliche Fähigkeit oder externe Quelle.
- Ein Agentenname erzeugt für sich allein keine technische Unabhängigkeit.
- Die Visualisierung speichert keinen dauerhaften Arbeitszustand.
- Der Mensch bleibt für Ziele, Freigaben und materielle Entscheidungen verantwortlich.

### Bestehender Paket-Prototyp

1. Lies [WORKSHOP.md](WORKSHOP.md).
2. Verwende [adviser/ADVISER.md](adviser/ADVISER.md) als Einstieg in die erste Fassung.
3. Sieh dir [package-core/PACKAGE_TEMPLATE](package-core/PACKAGE_TEMPLATE) an.
4. Probiere eines der Pakete unter [examples](examples) aus.
5. Validiere das Repository mit `python scripts/validate_workshop.py`.

### Lizenz

Dokumentation, Methoden, Prompts, Beispiele und visuelle Materialien stehen unter [CC BY 4.0](LICENSE-CONTENT). Ausführbarer Code und Tests stehen unter der [MIT-Lizenz](LICENSE-CODE). Weitere Informationen enthält [LICENSING.md](LICENSING.md).

