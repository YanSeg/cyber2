# Iteration 1

### 1.1 OWASP (Open Web Application Security Project)

**Pourquoi la liste évolue elle dans le temps ?** 

elle évolue en fonction des nouvelles menaces, des vulnérabilités découvertes et des avancées dans le domaine de la sécurité des applications web. Cette évolution est nécessaire pour assurer une protection efficace contre les menaces toujours changeantes auxquelles sont confrontées les applications web.

**Problème:**
Manque de vérification des données sur un formulaire web

**Catégorie(s) OWASP et explication:**
Injection 
Cross site Scripting
Conception non sécurisée(?)

### 1.2 Exemple problème 

Liste de problèmes:
 - Les extensions sont installées avec les privilèges de l'utilisateur et sans "sandbox"
 - N'importe qui peut déposer une extension sur le marketplace sans plus de backup check
 - Les extensions peuvent avoir des url quasi-similaire (typosquatting)
 - Les extensions peuvent avoir des noms exactement similaires (pas de displayName unique)

 ### 1.3 CVE (Common Vulnerabilities and Exposures)

C'est un système utilisé pour identifier de manière unique et normaliser les noms des vulnérabilités et des expositions connues en matière de sécurité de l'information. L'objectif de CVE est de fournir une méthode normalisée permettant aux organisations et aux chercheurs en sécurité de discuter et de partager des informations sur les vulnérabilités, facilitant ainsi une meilleure coordination des efforts de sécurité entre différentes plateformes et organisations.

Voici comment fonctionne le système CVE :

**Identification :** Lorsqu'une vulnérabilité ou un problème de sécurité est découvert, il se voit attribuer un identifiant CVE unique. Cet identifiant se compose du préfixe "CVE-" suivi de l'année et d'un numéro de séquence (par exemple, CVE-2024-12345). Cet identifiant est utilisé comme référence pour la vulnérabilité dans les discussions, les rapports et les bases de données.

**Description :** Chaque identifiant CVE est accompagné d'une description détaillée de la vulnérabilité, comprenant des informations telles que les logiciels concernés, l'impact potentiel et les stratégies d'atténuation. Cette description aide les professionnels de la sécurité et les développeurs à comprendre la nature et la gravité de la vulnérabilité.

**Publication :** Les identifiants CVE et leurs descriptions sont publiés dans la CVE List, qui est maintenue par la société MITRE Corporation, une organisation à but non lucratif qui gère des centres de recherche et développement financés par le gouvernement fédéral. La CVE List sert de référentiel central des vulnérabilités connues, accessible au public et aux communautés de sécurité du monde entier.

**Coordination :** Le système CVE facilite la collaboration entre les chercheurs en sécurité, les fournisseurs et les organisations en fournissant un moyen normalisé de référencer les vulnérabilités. Cette coordination est cruciale pour faire face efficacement aux menaces de sécurité, développer et déployer des correctifs et des mises à jour, et partager les meilleures pratiques d'atténuation.

**Suivi et remédiation :** Une fois qu'un identifiant CVE est attribué à une vulnérabilité, il peut être suivi par les organisations pour s'assurer que des mesures appropriées sont prises pour résoudre le problème. Cela peut impliquer le développement et le déploiement de correctifs, la mise en œuvre de contrôles de sécurité ou la mise à jour de configurations pour atténuer le risque posé par la vulnérabilité.

En résumé, le système CVE joue un rôle essentiel dans l'amélioration de la posture de sécurité des logiciels et des systèmes en favorisant la transparence, la collaboration et la responsabilité dans la gestion des vulnérabilités de sécurité.
