

  <h1>⚽ FBref Top 5 Leagues Stats Scraper</h1>

  <p>Ce projet est un script Python asynchrone conçu pour extraire automatiquement les statistiques des cinq grands championnats européens de football (Premier League, La Liga, Bundesliga, Serie A et Ligue 1) à partir du site <a href="https://fbref.com" target="_blank" rel="noopener">FBref</a>. Le script parcourt plusieurs saisons, de 2017 à 2025, et exporte les données collectées dans des fichiers CSV prêts à être analysés.</p>

  <h2>🚀 Fonctionnalités</h2>
  <p>Le script permet d’automatiser la récupération de statistiques détaillées sur les joueurs. Il prend en charge les cinq principales ligues européennes et plusieurs catégories statistiques. L’extraction est effectuée de manière asynchrone, ce qui permet un gain de performance important. Les données sont ensuite enregistrées au format CSV, avec un fichier généré pour chaque catégorie de statistiques.</p>

  <h2>📂 Catégories disponibles</h2>
  <p>Plusieurs types de statistiques sont extraits par le script :</p>
  <ul>
    <li><strong>Possession</strong> : touches, dribbles, pertes de balle, passes reçues, etc.</li>
    <li><strong>Passing</strong> : passes totales, passes réussies, distance parcourue, passes progressives, etc.</li>
    <li><strong>GCA (Goal and Shot Creating Actions)</strong> : actions menant à un tir ou à un but.</li>
    <li><strong>Shooting</strong> : tirs, buts, tirs cadrés, xG, npxG, etc.</li>
    <li><strong>Playing Time</strong> : minutes jouées, titularisations, matchs complets, etc.</li>
  </ul>
  <p>Chaque catégorie est téléchargée et exportée séparément pour faciliter l’analyse.</p>

  <h2>🧩 Technologies utilisées</h2>
  <p>Le projet est entièrement développé en Python et s’appuie sur les bibliothèques suivantes :</p>
  <ul>
    <li><strong>BeautifulSoup4</strong> pour l’analyse du contenu HTML.</li>
    <li><strong>crawl4ai</strong> pour simuler le navigateur.</li>
    <li><strong>asyncio</strong> pour la gestion des tâches concurrentes.</li>
    <li><strong>csv</strong> pour l’écriture des fichiers de sortie.</li>
  </ul>

  <h2>⚙️ Installation</h2>
  <p>Avant d’exécuter le script, assure-toi d’avoir <strong>Python 3.10</strong> ou une version plus récente installé sur ton système.</p>
  <p>Les bibliothèques nécessaires à l’exécution du projet sont :</p>
  <ul>
    <li><code>beautifulsoup4</code></li>
    <li><code>crawl4ai</code></li>
  </ul>
  <p>Pour installer <code>crawl4ai</code>, suis les instructions disponibles sur le site officiel : <a href="https://docs.crawl4ai.com" target="_blank" rel="noopener">https://docs.crawl4ai.com</a></p>

  <h2>🧠 Utilisation</h2>
  <p>L’exécution du script se fait simplement en lançant la commande suivante dans le terminal :</p>
  <pre><code>python3 groupe_8_github.py</code></pre>
  <p>Par défaut, le script parcourt automatiquement les saisons de <strong>2017 à 2025</strong>, les cinq ligues principales (Premier League, La Liga, Bundesliga, Serie A, Ligue 1) et plusieurs catégories de statistiques.</p>
  <p>L’utilisateur peut toutefois personnaliser facilement le comportement du script en modifiant les paramètres dans le code : la plage des <strong>saisons</strong> à analyser, la liste des <strong>ligues</strong> concernées, et les <strong>catégories</strong> de statistiques à extraire. Cela permet d’obtenir uniquement les données souhaitées sans avoir à relancer l’ensemble du processus.</p>

  <h2>📁 Structure des fichiers exportés</h2>
  <p>Chaque fichier CSV contient un ensemble cohérent de colonnes correspondant aux informations extraites. Parmi les colonnes communes, on retrouve le nom du joueur, son équipe, la saison, la ligue, ainsi que d’autres données spécifiques à chaque catégorie (comme le nombre de tirs, de passes réussies ou les minutes jouées).</p>
  <p>Ces fichiers peuvent être ouverts directement dans Excel, Google Sheets, ou utilisés dans un notebook Python pour une analyse approfondie (par exemple avec pandas).</p>

  <h2>⚠️ Remarques importantes</h2>
  <p>Le scraping de données sur FBref dépend de la structure HTML du site. Si FBref modifie sa mise en page ou ses identifiants de balises, le code pourrait nécessiter une mise à jour pour continuer à fonctionner correctement.</p>
  <p>Le module <code>crawl4ai</code> a besoin d’un accès Internet et le processus peut être relativement long, surtout en raison du grand nombre de saisons et de ligues traitées.</p>
  <p>Enfin, il est important de respecter les conditions d’utilisation de FBref. Ce script est destiné à un usage éducatif et non commercial.</p>

  <h2>🧑‍💻 Auteurs</h2>
  <p class="authors">Ce projet a été développé par <strong>Ibrahim</strong>, <strong>Stephen</strong> et <strong>Elom</strong>, trois passionnés de data et de football. Vous pouvez nous retrouver sur GitHub pour suivre nos travaux et contributions à d’autres projets.</p>

  <h2>⭐ Support</h2>
  <p>Si ce projet vous a été utile, n’hésitez pas à lui attribuer une étoile sur GitHub ⭐ et à proposer des suggestions d’améliorations ou des pull requests. Cela aide à faire évoluer le projet et à améliorer la qualité du code.</p>

</body>
</html>

