<h1>📘 INSTRUCTION — Extraction de statistiques de football (FBref)</h1>

<h2>1️⃣ Comment exécuter le code</h2>

<ol>
  <li>Exécute le script avec :</li>
</ol>

<pre><code>python3 groupe_8_github.py
</code></pre>

<p>Le script va automatiquement lancer le scraping et créer plusieurs fichiers CSV dans le même dossier.</p>

<hr>

<h2>2️⃣ Durée d’exécution</h2>
<p>
  Le script prend <strong> 6 minutes pour exécuter le scrapping pour une catégorie. </strong>
  
  Et il prend <strong> 30 minutes pour toutes les catégories.</strong>
</p>

<hr>

<h2>3️⃣ Modifications possibles</h2>

<p>L’utilisateur peut facilement modifier les paramètres suivants :</p>

<ul>
  <li><strong>Les saisons à analyser (ligne 17 du code) </strong>  
    <pre><code>years = range(2017, 2025)</code></pre>
    <p>(par exemple <code>range(2020, 2023)</code> pour réduire le temps d’exécution)</p>
  </li>

  <li><strong>Les catégories de statistiques à extraire (ligne 158 du code) </strong>  
    <pre><code>categories = ["possession", "passing", "gca", "shooting", "playingtime"]</code></pre>
    <p>(tu peux retirer ou ajouter des catégories selon ce que tu veux récupérer)</p>
  </li>

  <li><strong>Les ligues concernées (ligne 17 du code) </strong>  
    <pre><code>leagues = {
    "Premier-League": "9",
    "La-Liga": "12",
    "Bundesliga": "20",
    "Serie-A": "11",
    "Ligue-1": "13"
}</code></pre>
    <p>(tu peux enlever une ligue ou en ajouter si tu connais son identifiant FBref)</p>
  </li>
</ul>

<hr>

<h2>4️⃣ Fonctionnement global du code</h2>

<p>Le script effectue les actions suivantes :</p>
<ol>
  <li><strong>Parcourt automatiquement les saisons</strong> de 2017 à 2024.</li>
  <li><strong>Scrape les données</strong> depuis le site 
    <a href="https://fbref.com" target="_blank">FBref.com</a> pour les 5 grands championnats européens.
  </li>
  <li><strong>Récupère les statistiques des joueurs</strong> pour plusieurs catégories (possession, passes, tirs, etc.).</li>
  <li><strong>Regroupe et enregistre les données</strong> dans des fichiers CSV, un par catégorie.</li>
</ol>

<p>
  Chaque ligne du CSV correspond à un joueur, avec des informations comme son nom, son équipe, la saison, la ligue et les statistiques détaillées.
</p>
