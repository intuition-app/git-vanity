# Too Big To Fail - koa

Largest Commit (Non-Merge)

Author | SHA | Message | Total Lines Changed
--- | --- | --- | ---
TJ Holowaychuk | c699c75 | add koa Request / Response objects and delegation. | 5205
Gilles De Mey | d394724 | test: Use Jest (#981) | 1605
Michaël Zasso | b5c09a1 | test: fix style issues | 1280
broucz | 4b1a1da | test: switch all functions to arrow functionsclose | 1239
Tejas Manohar | 9f27c1c | refactor to use ES6 constchange var to const for s | 1110
Slobodan Stojanovic | b08facb | Fix indentation and add .eslint rulescloses #555 | 633
jongleberry | 2e8cdab | support async functionscloses #530closes #415 | 521
Jonathan Ong | 611dec1 | remove closure wrap in examples thanks to compose  | 400
pana | 1e38b13 | docs: update docs for koa v2update readme and requ | 386
dead_horse | e791100 | add more test case, fix req.idempotent | 255
Yiyu He | 162a5b3 | perf: lazy init cookies and ip when first time use | 188
Jeff Moore | 188c096 | Add Troubleshooting documentation (#921)* Move Com | 177
Felix Becker | ebb4850 | Remove co dependencycloses #558closes #557Change t | 175
Martin Iwanowski | 7f577af | meta: update AUTHORS (#1067) | 152
小雷 | 9146024 | feat: response.attachment append a parameter: opti | 143
Lee Bousfield | 6a14772 | Add support for flushing headers | 136
bhanuc | 17e98e4 | updated request.md and response.md | 136
Robin Pokorný | 340dd4f | Lint JavaScript in Markdown | 118
Tiago Ribeiro | a85f580 | Add full coverage | 91
Ruben Bridgewater | 8f047dd | fix: use non deprecated custom inspect (#1198)Cust | 77
blaz | d280122 | Add 2.0.0 Examples | 75
fengmk2 | 3e66157 | ctx.request.href: get full request url, include `p | 74
Xavier Damman | 2fda9dd | Added OpenCollective backers and sponsors (#748)*  | 73
Johan Bergström | c6c375c | Benchmarks: Table-fyHad to un-indent text for the  | 68
PlasmaPower | 54e58d3 | req: Cache the request IP | 67
mako-taco | 9fe483c | handle manually written responses | 57
Veselin Todorov | 6cd4c77 | context.throw supports Error instances | 55
initial-wu | 02feadc | Lazily initialize `request.accept` and delegate `c | 52
Ian Storm Taylor | 5931714 | make the second argument to throw properly optiona | 48
Robert Sköld | e900f0a | Use shorthand functionscloses #519 | 44
dead-horse | 3110314 | deps: upgrade all dependencies | 42
Yu Qi | 78832ff | bench: add bench for async/await (#1036) | 42
tmilewski | c2322f2 | remove .status=string #298 | 41
Martin fl0w Iwanowski | 0125878 | added setters for header and headers, fixes #991 | 40
Dmitry Mazuro | 9e8d6a3 | ocd | 40
Mengdi Gao | c2615ec | docs: capitalize K in word koa (#1126) | 38
C.T. Lin | 8586058 | implement ctx.origin | 38
Santiago Sotomayor | 0c438ed | unset content-type when the type is unknowncloses  | 37
Matthew Chase Whittemore | 789c30f | adding docs on how to add multiple middleware at o | 36
Pedro Pablo Aste Kompen | 0168fd8 | docs: Update middleware.gif (#1052) | 35
Saad Quadri | 40a6dd2 | docs: improve consistency in api code examples (#1 | 34
Matthew Mueller | 6847fe6 | added: ctx.state as the recommended namespace for  | 30
jeromew | 93351bf | Add req.host= | 28
JamesWang | 77ca429 | test: replace request(app.listen()) with request(a | 26
Equim | 08eb1a2 | docs: apply `Date.now()` to all docs (#988) | 24
Thiago Lagden | ee5af59 | replace apply by spread syntax (#971) | 24
Rui Marinho | 6d5f506 | Re-enable io.js support on .travis.ymlOn the 3rd o | 24
小菜 | 2cdbc52 | test&cov: add test case (#1211) | 22
Fangdun Cai | 18d753c | use Buffer.from instead (#946) | 22
Alexsey | 6baa411 | Error handling: on non-error throw try to stringif | 21
Riceball LEE | 53a4446 | expose the Application::handleRequest method (#950 | 21
Bryan Bess | 0192d21 | Increase test coverage | 21
Nick McCurdy | 53bea20 | Use eslint-config-koa (#1105) | 19
George Chung | cd5d6a1 | docs: reorganize "response.status=" section (#966) | 19
gyson | 1be333c | change respond() to a regular functionremove `yiel | 15
Bernie Stern | 6029064 | HTTP/2 has no status message (#1048) (#1049) | 13
Adam Lau | 21c0d82 | fix: subdomains should be [] if the host is an ip  | 13
yoshuawuyts | 41f77ed | readme: add flat badges and url variables | 13
Jason Macgowan | 4d42500 | docs: better demonstrate middleware flow (#1195) | 11
Clayton Ray | 2180839 | docs: Update koa-vs-express.md (#1230) | 10
Remek Ambroziak | 7f3d076 | docs: fix documentation to match new http-errors A | 10
Zack Tanner | 808768a | copy tweaks (#731) | 10
Yanick Rochon | d134fff | Fix issue when app.use() is called with empty valu | 10
Kwyn Alice Meagher | dce805b | Fix typo in example for Koa instantiationneed a ca | 10
Usman Hussain | 392e8aa | Koa routing (third party libraries support) (#1038 | 9
Travis Jeffery | e710b4b | add app.context docs | 9
Aaron Heckmann | 6392ee0 | return same object from request.queryBefore this c | 9
iamchenxin | fabf586 | Amend typo, request.is() return null|fasle|string. | 8
nswbmw | aac3d70 | update readme | 8
fundon | db7da4e | update bench casecloses #544 | 8
llambda | 30c8723 | Update Readme.md | 8
Jesus Rodriguez | 68843e0 | Remove unused imports and exports | 8
Jan Carlo Viray | a437329 | Fix misspelled word from "backwords" to "backwards | 8
Luke Bousfield | 6763021 | Fix context.inspect when called on the prototype ( | 7
mdemo | 520163f | add node 4.x on travis ci | 7
qingming | 2c507d3 | fix typo (#756) | 6
Louis DeScioli | d74802d | Standardizes instances of removeHeader to remove | 6
Douglas Christopher Wilson | 9dd99f5 | Parse Content-Type with "content-type" instead of  | 6
Adam L | e7f7db9 | Make `npm test` work with io.js | 6
urugator | d32623b | docs: Update error-handling.md (#1239)Docs incorre | 5
Kareem Kwong | 0a7856c | docs: Add note about overwriting charset in respon | 5
bananaappletw | 2da3dd4 | eslint: remove unused eslint-plugin-babel (#969) | 5
Darren Cauthon | 17ed10a | Fix word | 5
Taehwan, No | 1e81ea3 | docs: update babel setup (#1077) | 4
Chiahao Lin | 87cde82 | docs: modified examples using the wrong keyword (y | 4
song | bfce580 | Update Readme.md (#985)Change ```new Date``` to `` | 4
joehecn | 9248660 | test: fix spelling error (#972) | 4
Francisco Presencia | 3bbb74b | docs: added note about arrays (#964)Added note abo | 4
Avindra Goolcharan | 2a16426 | nit: fix grammar in generator deprecation warning  | 4
d3v | e0a0d9f | fix: v1 artifact "this" reference (#711) | 4
Marceli.no | fd83997 | TypoSignificant, but insignificant. Feel free to d | 4
Yazhong Liu | b969ecf | request: complete idempotent methodssee rfc2616: h | 4
Jesús Rodríguez Rodríguez | 8d1a340 | Fix typo on response.body test.Just a small typo. | 4
PatrickJS | adebc7d | update copyright year | 4
Qiming zhao | 14cdfb7 | fix doc, getter of type is delegated to requestSam | 4
Nathan Rajlich | 59d5de4 | Readme: add note about `gnode` to the ReadmeFor pe | 4
Jan Buschtöns | d750d0a | readme: fix various typos [no pluralization]L6: re | 4
Michał Gołębiowski-Owczarek | 9068316 | Update mgol's name in AUTHORS, add .mailmap (#1100 | 3
Jonas Zhang | e8a024c | docs: ddd Chinese docs link  for v2.x (#1092) | 3
haoxin | 49bdd1d | correct the link | 3

(Hiding 70 results)

Produced with [Git Vanity](https://github.com/intuition-app/git-vanity)

For meaningful analytics and reporting for Git, use [Intuition](https://intuition.app)

