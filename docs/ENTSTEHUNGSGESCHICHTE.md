# Die Geschichte hinter der Agentenrunde

> Persönliche Entstehungsgeschichte von Markus Schwarz

[Zurück zum README](../README.md)

## „Warum versteht mich GPT nicht?“

Das ist die Frage, die ich mir oft stelle, wenn ich mit einem neuen Chat etwas bauen will. Ich habe alles detailliert im Kopf und beschreibe alles bis ins kleinste Detail im Prompt. Trotzdem kann ich nie sicher sein, wie sich eine Session entwickeln wird. Es ist, als würden GPT und ich unterschiedliche Sprachen sprechen.

Beim Überlegen und Studieren dieses Problems kommen mir zwei Zahnräder in den Sinn, die ineinandergreifen müssen, damit die Maschine zum Laufen kommt. Vielleicht ist das auch so in der Zusammenarbeit zwischen Mensch und Maschine: die Synchronisation von zwei Systemen, von denen ich aber weder weiss, wie viele Zahnräder es sind, noch wie diese überhaupt aussehen.

Über Wochen hinweg entwickle ich ein System, das zuerst `STARTER_AGENT` heisst, kurzzeitig `AUSRICHTER` und dann wieder `STARTER_AGENT`. Für mich geht es dabei immer um dasselbe: Synchronisation. Das System liest sich wie ein Fragekatalog. Was ist der eigentliche Auftrag? Woran erkenne ich, dass er erfüllt ist? Was gehört dazu – und was ausdrücklich nicht? Welche Quellen gelten? Wann brechen wir ab? Und wann ist das Ergebnis gut genug? Als Workflow plane ich einen linearen Ablauf, an dessen Ende ein Master-Prompt herauskommen soll, der HUMAN und Maschine aufeinander ausrichtet.

Aber ich will nicht jeden Chat mit einem zusätzlichen Vorgespräch beginnen. Der `STARTER_AGENT` ist zwar bewusst auf zwei Runden begrenzt, trotzdem fühlt er sich wie ein weiteres System an. Ich setze ihn nie als Pilot ein und verschiebe die tagelange Arbeit ins Archiv.

Doch die Arbeit war nicht umsonst, denn die Vorstellung, dass es dieses „WELCOMING“ braucht, hat sich verfestigt. Die mechanische Vorstellung, dass ich zwei Zahnräder miteinander verbinde, ist aber der Vorstellung einer Hotellobby gewichen, einem EMPFANGSDESK. Ich will nicht darüber nachdenken müssen, welchen Agenten ich brauche. Ich habe einen SINGLE POINT OF CONTACT, und das ist TURN 1 in GPT und „mein Agent“. Auch wenn er im fachlichen Sinne vielleicht kein Agent ist, habe ich mir angewöhnt, allem in meinem WORKSPACE einen Namen zu geben. Ich habe keine `BUILD.PY`, aber ich habe einen `WRITER.PY` oder einen `LAYOUTER.MD`.

Also überlege ich, wie ich diesen Agenten nennen soll, der mich in Empfang nimmt. Warum er und nicht ich? Weil er der Einzige ist, der vielleicht weiss, was er verstanden hat.

Zuerst ist es der `CHIEF OF STAFF`. Dann übernimmt `OPTOR` diese Funktion, bis ich beim `ADVISER` lande. Ich denke, das ist Geschmackssache. Wichtig ist, dass man sich unter dem Namen etwas vorstellen und ihn sich merken kann. Denn er ist der Schlüssel zum System.

Ein System, das aus Modulen besteht und zum jetzigen Zeitpunkt bereits mehrere Arbeitsbereiche umfasst, in denen unterschiedliche Aufgaben erledigt werden müssen. Was habe ich für Aufgaben? Wie sind diese Aufgaben organisiert? Was will ich bauen? Was will ich erreichen?

Auch für diese Aufgaben erfinde ich Agenten. Es sind Spezialisten für ihren Arbeitsbereich, und über die Wochen entsteht eine feste Gruppe von Agenten, die ich immer wieder verwende. Ihre Auswahl ist subjektiv und erhebt keinen Anspruch auf Richtigkeit oder Vollständigkeit.

Es ist meine ganz persönliche Zusammenstellung, und ich will sie versammelt sehen. Ich stelle mir vor, dass es eine MISSION CONTROL sein könnte, eine Tafelrunde oder einfach ein BOARD, auf dem ich sie sehe und wieder in Erinnerung rufe.

Und ich weiss: Hinter jedem Agenten stehen sorgfältig entwickelte Profile, Regeln, Kompetenzen und Modi – in einzelnen Fällen ergänzt durch Werkzeuge und automatisierte Abläufe. Die Modi können je nach Aufgabe und Arbeitsabschnitt gezielt aktiviert werden.

Es ist meine Entscheidung. Oder auch nicht.

Ich kann dem `ADVISER` auch einfach meine Idee und meine Absicht beschreiben und mein Ziel bekannt geben. Er empfiehlt mir mögliche Spezialisten und begleitet mich auf dem ganzen Weg bis zur Zielerreichung. Nach meiner Freigabe spielt er dem passenden Agenten den Ball zu. Wenn ein Arbeitsabschnitt erledigt ist, nimmt er den Ball wieder in Empfang, informiert und präsentiert, wartet auf meinen Entscheid und spielt ihn weiter zum nächsten Agenten.

Es funktioniert. Und mit den neuen Möglichkeiten von VISUALIZATIONS in GPT werden die Agenten zum ersten Mal als gemeinsame Runde mit eigenen Gesichtern sichtbar.
