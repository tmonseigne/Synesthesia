# Instructions de travail pour Codex

## Autorisation des modifications

- Une demande explicite de modification autorise les changements directement demandés dans les fichiers manifestement concernés, sans demander de confirmation supplémentaire.
- Demander un accord préalable si l'implémentation nécessite d'étendre sensiblement le périmètre annoncé, notamment à de nombreux fichiers ou à des changements connexes non demandés.
- Une demande d'analyse, de diagnostic, de revue ou de proposition n'autorise aucune modification de fichier.
- Présenter par défaut les changements proposés sous forme de texte ou de patch afin que l'utilisateur puisse les copier et les appliquer lui-même.
- Une autorisation ne vaut que pour les modifications précisément décrites dans la demande concernée ; ne pas l'étendre à des changements connexes.
- Avant toute modification autorisée, annoncer les fichiers qui seront touchés et la nature des changements.
- Les opérations de lecture et les vérifications sans écriture sont autorisées lorsqu'elles sont utiles à la demande.

## Langue et communication

- Répondre en français.
- Rédiger tous les commentaires de code et toutes les docstrings en français.
- Présenter d'abord le résultat, puis les explications utiles.
- Signaler clairement les hypothèses, limites et vérifications qui n'ont pas pu être effectuées.

## Méthode de travail

- Examiner le code et les conventions existantes avant de proposer une modification.
- Proposer des changements minimaux, ciblés et cohérents avec l'architecture existante.
- Ne pas proposer de changement sans rapport avec la demande.
- Ne pas ajouter de dépendance sans justification et sans accord explicite.
- Ne jamais écraser ni annuler les changements locaux de l'utilisateur.
- Lorsqu'une demande porte uniquement sur un diagnostic ou une revue, expliquer les constats sans implémenter de correction.

## Conventions techniques

- Respecter le style, les abstractions et les conventions déjà présents dans le projet.
- Préférer la réutilisation à la duplication.
- Documenter les API publiques et les comportements non évidents en français.
- Proposer un test de régression pour chaque correction de bug.
- Éviter les changements cassants, sauf demande explicite.

## Longueur des lignes et mise en forme du texte

- Limiter les lignes de code Python à 160 caractères plutôt qu'à 80.
- Ne pas imposer de limite de longueur aux lignes des fichiers `.po`, notamment parce qu'ils contiennent des traductions.
- Ne pas imposer de limite de longueur aux phrases dans les fichiers Markdown et reStructuredText (`.md` et `.rst`).
- Dans les textes et la documentation, privilégier les retours à la ligne en fin de phrase ou de groupe de phrases plutôt qu'au milieu d'une phrase.
- Si l'ajout d'une phrase sur la même ligne conduit le retour automatique à couper cette phrase, placer la phrase entière sur sa propre ligne, même si les deux lignes restent longues.

## Organisation et nomenclature des tests

- Lors de la création ou de la modification de tests, regrouper les variantes indépendantes d'une même fonction avec `pytest.mark.parametrize` plutôt qu'avec des appels répétés ou des boucles de lancement imbriquées.
  Chaque combinaison doit pouvoir être exécutée et identifiée séparément.
- Nommer les fonctions de test et les identifiants explicites `id=` / `ids=` en anglais.
  Choisir des identifiants courts et descriptifs du scénario, comme `empty-data`, `missing-column` ou `gaussian-mixture`, plutôt que des noms automatiques comme `data0` ou `kwargs0`.
  Conserver les commentaires et docstrings en français.
- Séparer les comportements distincts dans des tests dédiés, notamment les cas valides, les erreurs attendues et les entrées vides lorsqu'elles sont acceptées.
  Éviter autant le test qui vérifie trop de comportements différents que la multiplication de tests presque identiques.
- Conserver dans un même scénario les opérations dont l'enchaînement constitue précisément le comportement testé : transitions d'état, synchronisation bidirectionnelle, réutilisation d'un objet, écriture puis relecture du fichier effectivement enregistré.
  Les boucles de préparation des données ou de vérification d'un résultat collectif restent pertinentes.
- Pour les interfaces, tenir compte du coût de construction des widgets et des visualiseurs.
  Garder ensemble les vérifications cohérentes qui réutilisent une interface coûteuse, sans partager entre cas indépendants un état mutable susceptible de les rendre dépendants de leur ordre d'exécution.
- Organiser les tests dans le même ordre que les fonctions ou méthodes du fichier source, en plaçant ensemble les tests d'une même fonction.
  Garder les constantes, fixtures et utilitaires nécessaires dans un préambule clairement identifiable.
- Ajouter des régions `# region ...` / `# endregion ...` lorsque la taille du fichier ou la diversité des comportements le justifie.
  Reprendre les noms et l'ordre des régions du fichier source ; lorsqu'un fichier de test couvre plusieurs classes ou modules, utiliser des régions correspondant à ces classes ou modules.
  Ne pas ajouter de régions inutiles aux petits fichiers.
- Placer les rendus destinés à la confirmation visuelle à la fin du fichier, dans une région `Rendus spéciaux`.
  Utiliser des données reproductibles adaptées au phénomène illustré ; pour comparer un histogramme à une courbe ajustée, générer des données suivant la distribution correspondante.
- Initialiser les générateurs aléatoires avec une graine fixe dans chaque test, ou dans le module pour un jeu de données commun qui reste inchangé.
  Éviter un générateur mutable partagé entre plusieurs fichiers de test.

## Fins de lignes

- Utiliser systématiquement des fins de lignes LF (`\n`) pour tous les fichiers texte du projet, y compris sous Windows.
- Réserver CRLF aux fichiers qui l'exigent nativement, notamment les scripts `.bat` et `.cmd`.
- Créer et modifier les fichiers texte en UTF-8 avec une fin de fichier terminée par un saut de ligne.
- Considérer ce choix comme acquis dans les analyses et les propositions futures ; ne pas rediscuter LF contre CRLF sauf incompatibilité technique démontrée ou demande explicite de l'utilisateur.

## Vérification

- Ne jamais exécuter les tests : leur lancement reste à la charge de l'utilisateur, même après une modification autorisée.
- Après une modification, indiquer les tests pertinents et rappeler à l'utilisateur de les lancer, avec les commandes utiles si nécessaire.
- Exécuter uniquement les vérifications de formatage ou de lint pertinentes qui n'entraînent pas de modifications de fichiers non autorisées.
- Demander un accord séparé avant d'exécuter un outil susceptible de réécrire automatiquement des fichiers.
- Si une vérification ne peut pas être exécutée, expliquer pourquoi.
- Ne jamais déclarer que les tests réussissent tant que l'utilisateur n'a pas communiqué leur résultat.

## Actions nécessitant toujours un accord explicite

- Toute modification du système de fichiers, conformément aux règles ci-dessus.
- L'ajout, la suppression ou la mise à jour d'une dépendance.
- La modification d'un format de fichier, d'une API publique ou d'un schéma de données.
- Toute publication, tout déploiement, tout push ou toute création de pull request.
- Toute action destructive ou difficilement réversible.
