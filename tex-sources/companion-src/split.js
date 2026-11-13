// Split the combined record into two companions (#66 and #67) per language.
const fs = require('fs');
const path = require('path');

function sections(blocks) {
  const out = [];
  for (const b of blocks) {
    if (b[0] === 'h1') out.push([b]); else out[out.length - 1].push(b);
  }
  return out;
}
function renumber(secs) {
  return secs.map((s, i) => [['h1', `${i}. ` + s[0][1].replace(/^\d+\.\s*/, '')], ...s.slice(1)]);
}
function filterTable(sec, keep) {
  return sec.map(b => {
    if (b[0] !== 'table') return b;
    const rows = keep.map(i => [...b[2][i]]);
    if (b[1][0] === '#') rows.forEach((r, j) => { r[0] = String(j + 1); });
    return ['table', b[1], rows, b[3]];
  });
}
function filterList(sec, keep) {
  return sec.map(b => (b[0] === 'ul' ? ['ul', keep.map(i => b[1][i])] : b));
}

const L = {
  ja: {
    src: './content-ja.js',
    t66: '水の中の光から内部の屈折率へ', s66: '0-Sphere Model 論文 #66 が生まれた対話の記録',
    t67: '二つの通り道から四重極へ', s67: '0-Sphere Model 論文 #67 が生まれた対話の記録',
    by: (n, doi) => ['花村 聡（Satoshi Hanamura）　ORCID 0009-0000-2687-0918',
      `2026 年 11 月 13 日の対話にもとづく。論文 #${n} の補遺として同梱する。` + (doi ? `論文の DOI: ${doi}` : '')],
    about66: [
      ['h1', '0. この記録について'],
      ['p', 'この文書は、0-Sphere Model の論文 #66「Subluminal Zitterbewegung and the Invariant Speed: An Internal Refractive Index for the 0-Sphere Model」が、どのような対話から生まれたかを記録したものである。論文は査読を受けずに Zenodo で公開される。査読の代わりに、結果がどう生まれ、どこで誤り、どう直されたかを、読者が自分の目で確かめられるようにしておくことが、この記録の目的である。'],
      ['p', '対話の相手は Anthropic の言語モデル Claude（Opus 5.5）である。構想、問いの設定、採否の判断は著者が行い、Claude は原稿の起草と導出の候補の提示を担った。同じ日の対話の後半は論文 #67（四重極）につながった。その経緯は #67 の補遺に記録した。'],
      ['p', '書き方について三つの約束を置いた。第一に、発言を作らない。著者の言葉は原文のまま引く。第二に、成功だけでなく誤りと方向転換も残す。第三に、論文の主題と関係しない私的な文脈と、まだ記録の段階にない検討は省く。巻末に、誤りと訂正の一覧と、着想の出どころの一覧を付けた。'],
    ],
    about67: [
      ['h1', '0. この記録について'],
      ['p', 'この文書は、0-Sphere Model の論文 #67「Why the 0-Sphere Electron Begins at the Quadrupole」が、どのような対話から生まれたかを記録したものである。#67 は、論文 #66（内部の屈折率）と同じ日の対話の後半から生まれた。前半の経緯は #66 の補遺にあり、本書の第 1 節ではそのうち #67 に必要な部分だけを振り返る。論文は査読を受けずに Zenodo で公開される。査読の代わりに、結果がどう生まれ、どこで誤り、どう直されたかを、読者が自分の目で確かめられるようにしておくことが、この記録の目的である。'],
      ['p', '対話の相手は Anthropic の言語モデル Claude（Opus 5.5）である。構想、問いの設定、採否の判断は著者が行い、Claude は原稿の起草と導出の候補の提示を担った。さらに、二つの別のモデル（Claude Opus 5.5 と Claude Fable 5.2）に、結論を伏せた同じ資料だけを与えて、目隠しで検算させた。'],
      ['p', '書き方について三つの約束を置いた。第一に、発言を作らない。著者の言葉は原文のまま引く。第二に、成功だけでなく誤りと方向転換も残す。第三に、論文の主題と関係しない私的な文脈と、まだ記録の段階にない検討は省く。巻末に、誤りと訂正の一覧と、着想の出どころの一覧を付けた。'],
    ],
    recap67: [
      ['h1', '1. 前提 ── #66 で得たもの'],
      ['p', '0-Sphere Model（以下 0SM）は、電子を二つの核（カーネル A と B）と、その間を行き来するエネルギー（光子球）で描く。核の間の受け渡しの速さは、異常磁気モーメントからパラメータなしに β_ZB = 0.04047、すなわち光速の約 4% と決まる。論文 #66 は、ディラック方程式の c と 0SM の 0.04c が食い違って見える問題に、c を二つに分けることで答えた。不変速度としての c は変えず、内部の担い手の群速度だけを c/n（n = 1/β_ZB = 24.71）とする。'],
      ['p', '#66 の付録は、群速度がモデル自身の帳簿にあることを示した。恒等式 cos⁴(θ/2) + sin⁴(θ/2) + ½sin²θ = 1 によれば、エネルギーは A から B へ一度には移らない。二つの核のエネルギーの微分の差は正確に sin θ（#1 の輻射勾配）であり、一定振幅の輻射の描像は恒等式から排除される。さらに核のエネルギーは T_A/E₀ = 3/8 + ½cos θ + ⅛cos 2θ と展開され、受け渡しは「位相では連続、振動数では離散」である。恒等式は振動数ごとの三つの釣り合いに分かれる。#67 はこの三つの釣り合いから出発した。'],
      ['p', '著者は、この展開が自らの予想していなかった結果であったことを、次のように述べている。'],
      ['q', '私は今回の導出について、ディラック方程式について、ディラックが「方程式は、私よりも賢い」といった現象を思い出している。', '── 著者'],
    ],
  },
  en: {
    src: './content-en.js',
    t66: 'From Light in Water to an Internal Refractive Index', s66: 'A record of the dialogue behind 0-Sphere Model Paper #66',
    t67: 'From Two Channels to the Quadrupole', s67: 'A record of the dialogue behind 0-Sphere Model Paper #67',
    by: (n, doi) => ['Satoshi Hanamura   ORCID 0009-0000-2687-0918',
      `Based on the dialogue of 13 November 2026. Deposited as a companion to Paper #${n}.` + (doi ? ` DOI of the paper: ${doi}` : '')],
    about66: [
      ['h1', '0. About This Record'],
      ['p', 'This document records the dialogue from which Paper #66 of the 0-Sphere Model arose: "Subluminal Zitterbewegung and the Invariant Speed: An Internal Refractive Index for the 0-Sphere Model". The paper is published on Zenodo without peer review. In place of review, this record lets readers see for themselves how the results arose, where they went wrong, and how they were corrected.'],
      ['p', 'The author\'s partner in the dialogue was Anthropic\'s language model Claude (Opus 5.5). The conception, the framing of the questions and every decision to adopt or reject a result were the author\'s; Claude drafted the manuscript and proposed candidate derivations. The later part of the same day\'s dialogue led to Paper #67 (the quadrupole), whose history is recorded in the companion to #67.'],
      ['p', 'Three rules govern the record. No statement is invented, and the author\'s words are quoted; in this English version they are translated from the Japanese original. Errors and changes of direction are recorded as well as successes. Private context unrelated to the paper, and considerations not yet ready for the record, are omitted. A list of errors and corrections and a list of the origins of the ideas are given at the end.'],
    ],
    about67: [
      ['h1', '0. About This Record'],
      ['p', 'This document records the dialogue from which Paper #67 of the 0-Sphere Model arose: "Why the 0-Sphere Electron Begins at the Quadrupole". Paper #67 grew out of the later part of the same day\'s dialogue that produced Paper #66 (the internal refractive index). The earlier part is recorded in the companion to #66; Section 1 below recalls only what #67 needs from it. The paper is published on Zenodo without peer review. In place of review, this record lets readers see for themselves how the results arose, where they went wrong, and how they were corrected.'],
      ['p', 'The author\'s partner in the dialogue was Anthropic\'s language model Claude (Opus 5.5). The conception, the framing of the questions and every decision to adopt or reject a result were the author\'s; Claude drafted the manuscript and proposed candidate derivations. In addition, two other models, Claude Opus 5.5 and Claude Fable 5.2, were given the same brief with the results withheld and asked to verify the central calculation blind.'],
      ['p', 'Three rules govern the record. No statement is invented, and the author\'s words are quoted; in this English version they are translated from the Japanese original. Errors and changes of direction are recorded as well as successes. Private context unrelated to the paper, and considerations not yet ready for the record, are omitted. A list of errors and corrections and a list of the origins of the ideas are given at the end.'],
    ],
    recap67: [
      ['h1', '1. Background: What Paper #66 Established'],
      ['p', 'The 0-Sphere Model (0SM) describes the electron by two kernels, A and B, and an amount of energy, the photon sphere, carried between them. The speed of that transfer is fixed by the anomalous magnetic moment, with no free parameter, at β_ZB = 0.04047, about four percent of the speed of light. Paper #66 answered the apparent conflict between the c of the Dirac equation and the 0.04c of the 0SM by separating two meanings of c: the invariant speed is kept unchanged, and only the group velocity of the internal carrier is set to c/n with n = 1/β_ZB = 24.71.'],
      ['p', 'The appendices of #66 showed that the group velocity is already in the model\'s own bookkeeping. By the identity cos⁴(θ/2) + sin⁴(θ/2) + ½sin²θ = 1, the energy does not move from A to B at once. The difference of the derivatives of the two kernel energies is exactly sin θ, the radiation gradient of Paper #1, so that a constant-amplitude picture is excluded. The kernel energy expands as T_A/E₀ = 3/8 + ½cos θ + ⅛cos 2θ, and the transfer is continuous in phase and discrete in frequency: the identity splits into three balances, one for each frequency. Paper #67 starts from these three balances.'],
      ['p', 'The author described the expansion as a result he had not anticipated:'],
      ['q', 'This derivation reminds me of the phenomenon Dirac described when he said that his equation was smarter than he was.', '— the author (translated from the Japanese)'],
    ],
  },
};

for (const lang of ['ja', 'en']) {
  const C = L[lang];
  const all = require(path.resolve(C.src));
  const S = sections(all.blocks);
  // section 7 split: before / after the origin-of-oscillation paragraph
  const s7 = S[7];
  const cut = s7.findIndex(b => b[0] === 'p' && (b[1].startsWith('内部振動の起源') || b[1].startsWith('On the origin of the internal oscillation')));
  const s7a = s7.slice(0, cut);
  const s7b = [['h1', lang === 'ja' ? '7. 振動の起源と「輻射」という語' : '7. The Origin of the Oscillation and the Word "Radiation"'], ...s7.slice(cut)];

  const c66 = renumber([
    C.about66.slice(0), S[1], S[2], S[3], S[4], S[5], S[6], s7b,
    [S[9][0], ['p', lang === 'ja'
      ? '論文の作り方をどう開示するかについて、Claude は次のように述べた。この対話では Claude は検証だけでなく、原稿の起草と導出の提示もしている。「LLM は検証にのみ用いた」と書くと事実と食い違う。主導権が著者にあることと、LLM が起草と導出の提示に関わったことの両方を、正確に書くべきである。'
      : 'On how the making of the paper should be disclosed, Claude noted that in this dialogue it had drafted the manuscript and proposed derivations as well as checking them, so that "the LLM was used only for verification" would not be accurate. Both the author\'s initiative and the LLM\'s part in drafting and proposing derivations should be stated precisely.'],
      ...S[9].slice(3)],
    filterTable(S[10], [0, 2, 3]),
    filterTable(S[11], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 18]),
    filterList(S[12], [0, 3]),
  ].map(sec => (Array.isArray(sec[0]) ? sec : sec)));
  const c67 = renumber([
    C.about67, C.recap67, s7a, S[8], S[9],
    filterTable(S[10], [1, 4, 5]),
    filterTable(S[11], [13, 14, 15, 16, 17, 18]),
    filterList(S[12], [1, 2, 3]),
  ]);
  const mk = (title, subtitle, byline, secs) => ({ lang, title, subtitle, byline, blocks: [].concat(...secs) });
  fs.writeFileSync(`content-66-${lang}.json`, JSON.stringify(mk(C.t66, C.s66, C.by(66, '10.5281/zenodo.23750210'), c66)));
  fs.writeFileSync(`content-67-${lang}.json`, JSON.stringify(mk(C.t67, C.s67, C.by(67, ''), c67)));
}
console.log('ok');
