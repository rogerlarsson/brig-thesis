# Einleitung {#sec:SEC01_EINLEITUNG}

## Motivation {#sec:SEC02_MOTIVATION}

Der Austausch von Dokumenten beziehungsweise Dateien wurde früher hauptsächlich
über Datenträger (Diskette, USB--Stick) oder E--Mail durchgeführt. Mit dem
Aufkommen der Cloud--Lösungen der letzten Jahre werden Dateien immer öfters
über Cloud--Dienste, wie beispielsweise Apple iCloud, Dropbox, Microsoft
OneDrive oder Google Drive, ausgetauscht.

Diese Dienste basieren auf einer zentralen Architektur und ermöglichen dem
Benutzer, seine Dateien über mehrere Computer hinweg zu synchronisieren und mit
Freunden --- oder im geschäftlichen Umfeld mit Partnern --- auszutauschen.
Hierbei ist man in der Regel auf die Verfügbarkeit des jeweiligen Dienstes
angewiesen. Fällt der Dienst aus oder wird beispielsweise von
Strafverfolgungsbehörden geschlossen
(Megaupload--Schließung[^FN_MEGAUPLOAD_TAKEDOWN]), bleibt einem der Zugriff auf
die eigenen Dateien verwehrt.

[^FN_MEGAUPLOAD_TAKEDOWN]: Hinweise zur Schließung von Megaupload: <https://de.wikipedia.org/w/index.php?title=Megaupload&oldid=161927073>

Auch wenn das Aufkommen dieser Dienste auf den ersten Blick eine Abhilfe sein
mag, so werden beim genaueren Hinsehen Risiken und Nachteile, welche erst
durch Aufkommen dieser Dienste entstanden sind, deutlich sichtbar. Eines der
Hauptprobleme ist, aufgrund mangelnder Transparenz, der Schutz der Daten
beziehungsweise der Privatsphäre.

Hier muss dem Dienstanbieter vollständig vertraut werden, da nicht bekannt ist
welche Drittparteien Zugriff auf die Daten haben. Dies mag bei der persönlichen
Musik--Sammlung --- im Gegensatz zur Speicherung sensibler medizinischer oder
finanzieller Unterlagen --- weniger ein Problem sein. Spätestens seit den
Snowden--Enthüllungen und des Bekanntwerdens vom PRISM--Überwachungsprogramm ist
offiziell bekannt[@bibgreenwald2013nsa], dass der Zugriff auf persönliche Daten
durch Drittparteien erfolgt ist, beziehungsweise erzwungen wurde. Neben dem
geduldeten oder rechtlich erzwungenen Zugriff durch Drittparteien, haben
Cloud--Speicher--Anbieter wie beispielsweise Dropbox in der Vergangenheit
immer wieder für Schlagzeilen gesorgt. Durch diverse Softwarefehler war
beispielsweise der Zugriff über mehrere Stunden mit beliebigen Passwörtern
möglich[^FN_DROPBOX_AUTH_BUG]. Ein weiterer Softwarefehler hat bei der
Aktivierung bestimmter Features Daten unwiderruflich
gelöscht[^FN_DROPBOX_DATA_CORRUPTION]. Daneben wird die Sicherheit von
Cloud--Speicher--Diensten in Studien bemängelt, vgl. [@bibfisitcloudsec].

[^FN_DROPBOX_AUTH_BUG]: Authentifizierungs--Bug: <https://blogs.dropbox.com/dropbox/2011/06/yesterdays-authentication-bug/>
[^FN_DROPBOX_DATA_CORRUPTION]: Selective--Sync--Bug: <https://plus.google.com/+MichaelArmogan/posts/E9sVnrLTB5C>

Will man Daten privat oder geschäftlich austauschen, so muss man sich in der
Regel auf einen Anbieter einigen. Hierbei stellt die
Fragmentierung[^FN_PROVIDER_FRAGMENTATION] der Cloud--Speicher--Anbieter den
Benutzer oft vor weitere Herausforderungen.

[^FN_PROVIDER_FRAGMENTATION]: Übersicht Online--Backup--Provider:

	<https://en.wikipedia.org/w/index.php?title=Comparison_of_online_backup_services&oldid=760247797>

Will man aus persönlichen Bedenken auf den Einsatz von Cloud--Speicher--Diensten
verzichten, bleibt einem immer noch die Möglichkeit, Dateien über E--Mail zu
versenden. Hier erschließt sich aber bei näherer Betrachtung ein ähnliches
Problem wie bei den Cloud--Speicher--Anbietern. Die Privatsphäre, beziehungsweise
der Schutz der Daten vor dem Zugriff durch Dritte, ist mangelhaft. Es gibt die
Möglichkeit E-Mails beispielsweise mittels Pretty Good Privacy (PGP) zu
verschlüsseln, jedoch ist der Einsatz und Aufwand für den Otto
Normalverbraucher schlichtweg zu kompliziert und wird daher kaum genutzt.

Der Austausch über einen Cloud--Speicher--Dienst oder E-Mail ist nichtsdestotrotz der
Quasi--Standard. Es gibt zwar technisch gesehen weitere Möglichkeiten, Daten
auch ohne eine zentrale Instanz auszutauschen, diese sind jedoch entweder
recht unbekannt, für den Otto Normalverbraucher unbenutzbar oder unsicher. Zu
den bekanntesten Vertretern gehören hier wahrscheinlich
Syncthing[^FN_SYNCTHING], git--annex[^FN_GIT_ANNEX] oder auch Resilio[^FN_RESILIO].

[^FN_SYNCTHING]: Syncthing: <https://syncthing.net/>
[^FN_RESILIO]: Resilio: <https://getsync.com/>
[^FN_GIT_ANNEX]: git--annex: <https://git-annex.branchable.com/>

Diese Ausgangssituation hat letztendlich nicht nur aus persönlichem Interesse
und mangels Alternativen dazu geführt, sich mit der Thematik näher zu befassen
und weitere Möglichkeiten zu erschließen. In Zusammenarbeit mit meinem
Kommilitonen, Christopher Pahl, wurde die Entwicklung an dem dezentralen
Dateisynchronisationswerkzeug »brig« gestartet, welches die aktuelle Situation
verbessern soll.

## Organisation und Schwerpunkte der Arbeit {#sec:SEC01_ORGANISATION_UND_SCHWERPUNKT_DER_ARBEIT}

**Projektschwerpunkte:**

Ziel ist es eine Software zu entwickeln, welche aktuelle Sicherheitsstandards
und Usability möglichst gut vereint und dabei ohne zentrale Instanz auskommt.

Aufgegliedert liegen die Schwerpunkte wie folgt:

*Vollständige Transparenz:* Der Benutzer soll vollständige Transparenz
bezüglich der Software und dem Entwicklungsprozess haben. Nur so lässt ich
eine vertrauenswürdige Implementierung gewährleisten.

*Aktuelle Sicherheitsstandards:* Die Software soll die Daten des Benutzers zu
jeder Zeit möglichst gut schützen. Hierzu sollen bewährte Sicherheitsstandards
verwendet werden.

*Möglichst intuitive Benutzung:* Der Benutzer soll von der
Sicherheitskomplexität so wenig wie möglich mitbekommen. Die Software soll dabei
jedoch mindestens so einfach nutzbar sein wie die heutzutage gängigen
Cloud--Dienste.

**Organisation:**

Die Basis für die Entwicklung der Software, Validierung einzelner Komponenten
und Prozesse, sowie die Ausarbeitung möglicher zukünftiger Konzepte stellen die
folgenden Arbeiten dar:

1) »brig«: Ein Werkzeug zur sicheren und verteilten Dateisynchronisation,
   *Christopher Pahl*
2) Sicherheitskonzepte und Evaluation dezentraler Dateisynchronisationssysteme
   am Beispiel »brig«, *Christoph Piechula*

Aktuell wird die Software im Rahmen der genannten Masterarbeiten bei *Prof.
Dr.-Ing. Thorsten Schöler* in der *Distributed Systems Group*[^FN_DSG] der
Hochschule Augsburg entwickelt.

[^FN_DSG]: Distributed Systems Group: <http://dsg.hs-augsburg.de>

Die vorliegende Arbeit hat dabei aufgrund des Umfangs des Gesamtprojekts
folgende Schwerpunkte, Fragestellungen und Ziele:

* Sensibilisierung von Entwicklern und Benutzern für die Thematik der sicheren
  Software. Warum ist sichere Software und Kryptographie für unsere Gesellschaft
  wichtig? Worauf ist bei der Implementierung zu achten, wie sind die Zusammenhänge?
* Zusammenhängende Betrachtung der Sicherheit von Software.
* Betrachtung der Sicherheitskonzepte, Vor-- und Nachteile zentraler und
  dezentraler Lösungen.
* Evaluation bisheriger Ansätze (Sicherheit, Usability) und Definition möglicher
  Verbesserungen, welche in die Weiterentwicklung und in den
  Entwicklungsprozess einfließen sollen.
* Betrachtung von Sicherheitskonzepten, welche für eine sichere, transparente
  und vertrauenswürdige Softwareentwicklung und Softwareverteilung essentiell sind.

## Zielgruppen und Einsatzszenarien {#sec:SEC01_ZIELGRUPPEN_UND_EINSATZSZENARIEN}

Da die Software nicht auf ein bestimmtes Fachgebiet begrenzt werden kann, ist
die Nutzung sowohl durch Individuen, Unternehmen als auch öffentliche
Einrichtungen möglich.

Aufgrund der Ausrichtung der Projektziele, sollen jedoch vor allem Benutzer mit
erhöhten Sicherheitsanforderungen von der Software profitieren. Hierzu gehören
neben einzelnen Individuen vor allem bestimmte Personengruppen wie
beispielsweise:

* Journalisten und Aktivisten
* Fachkräfte im medizinischen Bereich
* Fachkräfte in öffentlichen Einrichtungen

## Projektname und Lizenzierung {#sec:SEC01_PROJEKTNAME_UND_LIZENZIERUNG}

Der Name »brig« ist eine Anlehnung an das zweimastige Handelsschiff
*brigg*[^FN_BRIGG], welches gegen Ende des 18. Jahrhunderts zum Einsatz kam.
Die Namensanlehnung soll analog den dezentralen Transport von Daten darstellen.

[^FN_BRIGG]: Brigg Handelsschiff: <https://de.wikipedia.org/w/index.php?title=Brigg&oldid=155265558>

Aufgrund der Projektziele kommt als Lizenzierung die Open--Source--Lizenz[^FN_OPENSOURCE]
AGPLv3[^FN_AGPL] zum Einsatz. Denkbar wären jedoch im späteren Verlauf des
Projektes kombinierte Lizenzen für Unternehmen.

[^FN_OPENSOURCE]: Open--Source--Software: <https://de.wikipedia.org/w/index.php?title=Open_Source&oldid=162165962>

[^FN_AGPL]: AGPLv3 Lizenz: <https://www.gnu.org/licenses/agpl-3.0.de.html>
