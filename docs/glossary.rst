Glossaire
=========

Les termes sont regroupés par domaine afin de faciliter la consultation. Ils restent triés alphabétiquement à l’intérieur de chaque catégorie.

Neurosciences, perception et expérimentation
--------------------------------------------

.. glossary::
   :sorted:

   Anisotropie fractionnelle
      Indice dérivé de l'imagerie de diffusion qui décrit à quel point la diffusion de l'eau est orientée dans une direction privilégiée. Il est notamment utilisé comme indicateur de l'organisation de la substance blanche, sans mesurer directement le sens des connexions neuronales ni établir une relation causale.

   Chromesthésie
      Forme de synesthésie dans laquelle des sons ou des caractéristiques musicales déclenchent automatiquement des expériences colorées. Les associations peuvent varier fortement d'une personne à l'autre et ne définissent pas une conversion universelle entre son et couleur.

   Connectivité fonctionnelle
      Mesure statistique de la dépendance ou de la corrélation entre l'activité de différentes régions cérébrales au cours du temps. Elle indique que leurs activités covarient, mais ne démontre ni une connexion anatomique directe, ni le sens des échanges, ni une causalité.

   Correspondance intermodale
      Association systématique observée entre des caractéristiques appartenant à des modalités sensorielles différentes, par exemple entre un son aigu et une position visuelle élevée. Une correspondance de groupe n'implique pas une synesthésie ni une règle universelle valable pour chaque individu.

   Émotion perçue
      Émotion qu'un observateur attribue à un stimulus, par exemple considérer une musique comme joyeuse ou triste. Elle doit être distinguée de l'émotion effectivement ressentie par la personne qui l'écoute et de sa préférence pour le stimulus.

   IRMf (Imagerie par Résonance Magnétique fonctionnelle)
      Technique d'imagerie cérébrale estimant indirectement les variations d'activité neuronale, généralement à partir des changements d'oxygénation du sang. Elle permet d'étudier l'activité et la connectivité fonctionnelle de régions cérébrales avec une résolution temporelle limitée.

   Stimulus
      Élément présenté à un participant dans une expérience afin de provoquer ou mesurer une réponse. Il peut s'agir ici d'un son, d'un extrait musical, d'une couleur, d'une forme ou d'une combinaison contrôlée de ces éléments.

   Synesthésie
      Phénomène perceptif dans lequel un stimulus déclenche de manière automatique et relativement stable une expérience supplémentaire, par exemple une couleur associée à un son. Les associations sont individuelles et leur présence ne peut pas être déduite d'une simple préférence ou d'une correspondance perceptive de groupe.

   Synesthète
      Personne présentant une forme de synesthésie. Dans un contexte expérimental, il convient de distinguer une synesthésie simplement déclarée d'un statut évalué au moyen d'un protocole de cohérence ou d'autres critères définis par l'étude.

Analyse du signal et traitement audio
-------------------------------------

.. glossary::
   :sorted:

   Attaque
      Début d'un événement sonore, généralement caractérisé par une augmentation rapide de l'énergie ou une modification importante du spectre. La détection automatique des attaques (*onset detection*) permet de repérer temporellement des événements tels que des notes ou des impacts.

   Centroïde spectral
      Mesure décrivant le « centre de gravité » du spectre en fréquence. Pour des amplitudes spectrales :math:`X_k` associées aux fréquences :math:`f_k`, il peut s'écrire :math:`C = \frac{\sum_k f_k X_k}{\sum_k X_k}`. Une valeur élevée correspond généralement à un spectre contenant proportionnellement davantage d'énergie dans les hautes fréquences.

   DSP (Digital Signal Processing)
      Traitement numérique du signal. Ensemble des méthodes permettant d'analyser ou de transformer des signaux échantillonnés : filtrage, analyse fréquentielle, extraction de caractéristiques, détection d'événements, etc.

   Échantillonnage
      Conversion d'un signal continu en une suite de valeurs mesurées à intervalles temporels réguliers. La fréquence d'échantillonnage, exprimée en hertz, indique le nombre d'échantillons acquis par seconde.

   Fenêtre d'analyse
      Portion temporelle finie du signal utilisée pour calculer une mesure locale. Sa durée détermine un compromis entre résolution temporelle et fréquentielle ; deux fenêtres successives peuvent se chevaucher selon le pas temporel choisi.

   FFT (Fast Fourier Transform)
      Transformée de Fourier rapide. Famille d'algorithmes calculant efficacement la transformée de Fourier discrète d'un signal. Elle permet notamment d'obtenir, pour une fenêtre temporelle, une représentation de son contenu en fréquences appelée spectre.

   Flux spectral
      Mesure de la variation du spectre entre deux fenêtres temporelles successives. Une augmentation importante peut signaler un changement sonore rapide ou une attaque, mais la mesure peut également réagir au bruit ou à d'autres modifications du signal.

   Fréquence d'échantillonnage
      Nombre d'échantillons numériques représentant une seconde de signal, exprimé en hertz (Hz). Par exemple, une fréquence de 48 kHz correspond à 48 000 échantillons par seconde et par canal.

   Hauteur fondamentale
      Fréquence fondamentale :math:`f_0` associée à la périodicité principale d'un son et fortement liée à la hauteur tonale perçue lorsque celle-ci est définie. Son estimation peut devenir ambiguë ou impossible pour certains bruits, silences ou mélanges polyphoniques.

   Lissage
      Traitement réduisant les variations rapides d'une mesure au cours du temps. Il permet d'obtenir une animation plus stable, au prix d'une réponse potentiellement plus lente aux changements du signal.

   MFCC (Mel-Frequency Cepstral Coefficients)
      Coefficients cepstraux calculés sur une échelle de fréquences de type Mel, conçue pour approximer certaines propriétés de la perception auditive. Ils résument l'enveloppe spectrale d'un son et sont fréquemment utilisés comme descripteurs de timbre ou comme entrées d'algorithmes d'analyse audio.

   Normalisation
      Transformation destinée à ramener une mesure dans une plage ou une échelle commune afin de faciliter sa comparaison ou son utilisation. La méthode choisie doit être documentée car elle modifie la relation entre les données audio et les paramètres visuels.

   Pas temporel
      Intervalle séparant deux instants successifs auxquels une analyse est calculée. Avec des fenêtres chevauchantes, le pas temporel est inférieur à la durée de la fenêtre d'analyse et détermine en partie la résolution temporelle des mesures.

   RMS (Root Mean Square)
      Valeur quadratique moyenne utilisée ici comme mesure de l'énergie ou du niveau d'un signal audio. Pour :math:`N` échantillons :math:`x_n`, :math:`RMS = \sqrt{\frac{1}{N}\sum_{n=1}^{N} x_n^2}`. Elle ne représente pas directement la sonie perçue par l'auditeur.

   Sonie
      Intensité sonore telle qu'elle est perçue par l'être humain. Elle dépend notamment du niveau acoustique, du contenu fréquentiel et de la durée ; elle ne doit pas être assimilée directement à l'amplitude ou à l'énergie RMS du signal numérique.

   Spectre
      Représentation de la répartition d'un signal selon les fréquences. Il est généralement obtenu sur une fenêtre temporelle à l'aide d'une transformée de Fourier et sert de base au calcul de nombreux descripteurs audio.

   Transformée de Fourier
      Transformation mathématique décomposant un signal en composantes fréquentielles. Pour un signal numérique fini, on utilise généralement la transformée de Fourier discrète, souvent calculée efficacement au moyen d'une FFT.

Acoustique et musique
---------------------

.. glossary::
   :sorted:

   Classe de hauteur
      Regroupement de toutes les notes séparées par un nombre entier d'octaves et portant le même nom musical, par exemple tous les Do. Elle décrit la position cyclique d'une note dans l'octave indépendamment de son registre.

   Consonance
      Propriété perceptive ou musicale décrivant généralement une combinaison de sons perçue comme relativement stable ou harmonieuse dans un contexte donné. Elle dépend des intervalles, du timbre, du contexte musical et de facteurs culturels et ne constitue pas une grandeur acoustique unique.

   Hauteur tonale
      Perception permettant d'ordonner approximativement les sons du grave vers l'aigu. Elle est liée à la fréquence fondamentale pour de nombreux sons périodiques, mais constitue une propriété perceptive et non une simple mesure de fréquence.

   Mode majeur / mineur
      Organisation tonale reposant sur des relations d'intervalles caractéristiques autour d'une tonique. Les modes majeur et mineur peuvent influencer des jugements perceptifs ou émotionnels, mais ne suffisent pas à déterminer à eux seuls l'émotion d'un morceau ou une palette de couleurs.

   Polyphonie
      Présence simultanée de plusieurs notes ou voix musicales. Un signal polyphonique rend notamment l'estimation d'une hauteur fondamentale unique plus difficile qu'avec un son monophonique isolé.

   Tempo
      Vitesse d'organisation temporelle de la musique, généralement exprimée en battements par minute (BPM). Son estimation automatique à partir d'un signal complexe est un problème distinct de la simple détection d'attaques.

   Timbre
      Ensemble des propriétés perceptives permettant notamment de distinguer deux sons de même hauteur et de même niveau produits par des sources différentes. Il dépend de caractéristiques spectrales et temporelles et ne se réduit pas à un descripteur unique tel que les MFCC ou le centroïde spectral.

Colorimétrie et rendu visuel
----------------------------

.. glossary::
   :sorted:

   Calibration
      Procédure consistant à mesurer et régler un dispositif par rapport à une référence connue. Pour un écran, elle vise notamment à maîtriser la luminance et la reproduction des couleurs afin que les stimuli affichés soient comparables entre mesures ou dispositifs.

   Chroma
      En colorimétrie, attribut décrivant l'intensité ou la saturation apparente d'une couleur indépendamment, autant que possible, de sa clarté. Dans le cahier des charges, ce terme désigne une dimension colorimétrique et ne doit pas être confondu avec les descripteurs musicaux appelés *chroma*.

   CIELUV
      Espace colorimétrique défini par la CIE afin de représenter les couleurs de manière plus proche de leurs différences perceptives que l'espace RGB. Il permet notamment de calculer des distances entre couleurs, sous réserve d'utiliser une conversion et des conditions de référence définies.

   Gamut
      Ensemble des couleurs qu'un dispositif ou un espace colorimétrique est capable de représenter. Une couleur située hors du gamut d'un écran ne peut pas y être reproduite exactement.

   Palette
      Ensemble organisé de couleurs utilisables par le moteur de rendu. Dans Synesthesia, une palette peut être proposée par défaut ou définie dans un profil personnel ; elle ne représente pas nécessairement une correspondance perceptive universelle.

Modélisation, synchronisation et représentation
-----------------------------------------------

.. glossary::
   :sorted:

   Courbe de transfert
      Fonction transformant une mesure d'entrée en un paramètre de sortie. Dans Synesthesia, elle peut par exemple convertir une énergie audio normalisée en taille, luminosité ou vitesse d'un élément visuel, avec une relation linéaire ou non linéaire.

   Horodatage
      Association d'une donnée ou d'un événement à un instant précis. Dans Synesthesia, les mesures audio et les états visuels sont horodatés afin de conserver leur synchronisation pendant la lecture et l'export.

   Latence audio-visuelle
      Décalage temporel entre un événement audio et sa conséquence visuelle affichée. Elle résulte de l'acquisition ou du décodage, de la taille des blocs, de l'analyse DSP, de la planification des tâches et du rendu ; elle doit donc être mesurée de bout en bout.

   Profil de correspondance
      Ensemble versionné de règles et de paramètres transformant les mesures audio en attributs visuels. Il peut contenir des plages, seuils, courbes de transfert, palettes et autres réglages nécessaires pour reproduire un rendu.

   Sémantique
      Ensemble du sens attribué à une information ou à une représentation. Dans le cahier des charges, conserver la même sémantique de mesures signifie que les mêmes grandeurs, unités, conventions et significations sont utilisées en pré-analyse et en traitement direct.

Statistiques et méthodologie scientifique
-----------------------------------------

.. glossary::
   :sorted:

   Comparaisons multiples
      Situation statistique dans laquelle plusieurs hypothèses sont testées simultanément. La multiplication des tests augmente le risque d'obtenir au moins un résultat significatif par hasard et peut nécessiter une correction statistique adaptée.

   Médiation
      Hypothèse selon laquelle la relation entre deux variables passe en partie par une troisième variable. Dans les études musique-couleur citées, l'émotion peut par exemple être étudiée comme intermédiaire entre certaines caractéristiques musicales et les couleurs choisies.

   Réplication
      Réalisation d'une nouvelle étude visant à vérifier si un résultat scientifique peut être retrouvé avec de nouvelles données et, selon le protocole, dans des conditions identiques ou proches.

Logiciel, formats et licences
-----------------------------

.. glossary::
   :sorted:

   AGPLv3 (GNU Affero General Public License version 3)
      Licence libre de type *copyleft* imposant notamment de fournir le code source correspondant lors de la redistribution d'une version couverte. Elle étend cette obligation aux versions modifiées utilisées pour fournir un service à des utilisateurs par l'intermédiaire d'un réseau.

   Codec
      Procédé ou logiciel assurant l'encodage et le décodage d'un flux numérique, par exemple audio ou vidéo. Un codec peut appliquer une compression avec ou sans perte et se distingue du conteneur qui organise les différents flux d'un fichier multimédia.

   Copyleft
      Principe de licence libre imposant que certaines redistributions ou œuvres dérivées conservent les libertés accordées par la licence d'origine. Les obligations exactes dépendent de la licence concernée.
