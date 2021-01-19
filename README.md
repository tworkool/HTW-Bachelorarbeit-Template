## Vorlage Bachelorarbeit HTW Berlin - Fachbereich 2
Es handelt sich hierbei um eine inoffizielle LaTeX Vorlage für die Bachelorarbeit an der HTW Berlin für den Fachbereich 2, speziell Studiengang Ingenieur-Informatik. Die Vorlage wurde nach den Vorgaben aus dem Modul "Wissenschaftliches Arbeiten" erstellt. Ich hafte für keine formalen Fehler oder falsche Vorstellungen!
### Projektstruktur
Ordner `abb` ist für Bilder da (Bilder müssen mit `abb/[bildname]` eingebunden werden)
Ordner `code` kann für Codeausschnitte benutzt werden(noch nicht in Benutzung)
Ordner `pages` ist für alle .tex Inhaltsdateien da

Datei `ref.bib` ist das BibTex Literaturverzeichnis
Datei `abk.tex` ist für die Abkürzungen da(acronym package)
Datei `symb.tex` ist für Symbole da
Datei `vars.tex` ist für LaTeX Command Definitionen da, u.a. auch einfach Variablen

### Benutzung
Die Dokumente wurden mit XeLatex kompiliert, sollte aber auch mit PDFLatex gehen oder anderen gängigen Kompilierern.
Die Hauptdatei heißt `ba_template_htw.tex`.
Bevor kompiliert wird muss das HTW Logo [hier](https://corporatedesign.htw-berlin.de/logos/logo-htw-berlin/) runtergeladen werden, und in den Ordner `abb` unter dem Namen `logo_htw` gespeichert werden.
Die Bash Datei `CREATE_NOMENCLATURE` ist zur Erstellung des Abkürzungsverzeichnisses da(ist nur der Command zum erstellen der Verzeichnissdatei, kann also auch einfach kopiert werden). Wenn die Hauptdatei umbenannt wird muss der Command auch geändert werden.