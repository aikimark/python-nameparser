# -*- coding: utf-8 -*-
from __future__ import unicode_literals

SUFFIX_NOT_ACRONYMS = set([
    'dr',
    'esq',
    'esquire',
    'jr',
    'jr.',
    'jnr',
    'junior',
    'sr',
    'snr',
    '2',
    'i',
    'ii',
    'iii',
    'iv',
    'v',
])
"""

Post-nominal pieces that are not acronyms. The parser does not remove periods
when matching against these pieces.

"""
SUFFIX_ACRONYMS = set([
    '(ret)',
    '(ret.)',
    '(vet)',
    '8-vsb',
    'aas',
    'aba',
    'abc',
    'abd',
    'abpp',
    'abr',
    'aca',
    'acas',
    'ace',
    'acha',
    'acp',
    'ae',
    'ae',
    'aem',
    'afasma',
    'afc',
    'afc',
    'afm',
    'afm',
    'agsf',
    'aia',
    'aicp',
    'ala',
    'alc',
    'alp',
    'am',
    'amd',
    'ame',
    'amieee',
    'ams',
    'aphr',
    'apn aprn',
    'apr',
    'apss',
    'aqp',
    'arm',
    'arrc',
    'asa',
    'asc',
    'asid',
    'asla',
    'asp',
    'atc',
    'awb',
    'bca',
    'bcl',
    'bcss',
    'bds',
    'bem',
    'bem',
    'bls-i',
    'bpe',
    'bpi',
    'bpt',
    'bt',
    'btcs',
    'bts',
    'cacts',
    'cae',
    'caha',
    'caia',
    'cams',
    'cap',
    'capa',
    'capm',
    'capp',
    'caps',
    'caro',
    'cas',
    'casp',
    'cb',
    'cbe',
    'cbm',
    'cbne',
    'cbnt',
    'cbp',
    'cbrte',
    'cbs',
    'cbsp',
    'cbt',
    'cbte',
    'cbv',
    'cca',
    'ccc',
    'ccca',
    'cccm',
    'cce',
    'cchp',
    'ccie',
    'ccim',
    'cciso',
    'ccm',
    'ccmt',
    'ccna',
    'ccnp',
    'ccp',
    'ccp-c',
    'ccpr',
    'ccs',
    'ccufc',
    'cd',
    'cdal',
    'cdfm',
    'cdmp',
    'cds',
    'cdt',
    'cea',
    'ceas',
    'cebs',
    'ceds',
    'ceh',
    'cela',
    'cem',
    'cep',
    'cera',
    'cet',
    'cfa',
    'cfc',
    'cfcc',
    'cfce',
    'cfcm',
    'cfe',
    'cfeds',
    'cfi',
    'cfm',
    'cfp',
    'cfps',
    'cfr',
    'cfre',
    'cga',
    'cgap',
    'cgb',
    'cgc',
    'cgfm',
    'cgfo',
    'cgm',
    'cgm',
    'cgma',
    'cgp',
    'cgr',
    'cgsp',
    'ch',
    'ch',
    'cha',
    'chba',
    'chdm',
    'che',
    'ches',
    'chfc',
    'chfc',
    'chi',
    'chmc',
    'chmm',
    'chp',
    'chpa',
    'chpe',
    'chpln',
    'chpse',
    'chrm',
    'chsc',
    'chse',
    'chse-a',
    'chsos',
    'chss',
    'cht',
    'cia',
    'cic',
    'cie',
    'cig',
    'cip',
    'cipm',
    'cips',
    'ciro',
    'cisa',
    'cism',
    'cissp',
    'cla',
    'clsd',
    'cltd',
    'clu',
    'cm',
    'cma',
    'cmas',
    'cmc',
    'cmfo',
    'cmg',
    'cmp',
    'cms',
    'cmsp',
    'cmt',
    'cna',
    'cnm',
    'cnp',
    'cp',
    'cp-c',
    'cpa',
    'cpacc',
    'cpbe',
    'cpcm',
    'cpcu',
    'cpe',
    'cpfa',
    'cpfo',
    'cpg',
    'cph',
    'cpht',
    'cpim',
    'cpl',
    'cplp',
    'cpm',
    'cpo',
    'cpp',
    'cprc',
    'cpre',
    'cprp',
    'cpsc',
    'cpsi',
    'cpss',
    'cpt',
    'cpwa',
    'crde',
    'crisc',
    'crma',
    'crme',
    'crna',
    'cro',
    'crp',
    'crt',
    'crtt',
    'csa',
    'csbe',
    'csc',
    'cscp',
    'cscu',
    'csep',
    'csi',
    'csm',
    'csp',
    'cspo',
    'csre',
    'csrte',
    'csslp',
    'cssm',
    'cst',
    'cste',
    'ctbs',
    'ctfa',
    'cto',
    'ctp',
    'cts',
    'cua',
    'cusp',
    'cva',
    'cva[22]',
    'cvo',
    'cvp',
    'cvrs',
    'cwap',
    'cwb',
    'cwdp',
    'cwep',
    'cwna',
    'cwne',
    'cwp',
    'cwsp',
    'cxa',
    'cyds',
    'cysa',
    'dabfm',
    'dabvlm',
    'dacvim',
    'dbe',
    'dc',
    'dcb',
    'dcm',
    'dcmg',
    'dcvo',
    'dd',
    'dds',
    'ded',
    'dep',
    'dfc',
    'dfm',
    'diplac',
    'diplom',
    'djur',
    'dma',
    'dmd',
    'dmin',
    'dnp',
    'do',
    'dpm',
    'dpt',
    'drb',
    'drmp',
    'drph',
    'dsc',
    'dsm',
    'dso',
    'dss',
    'dtr',
    'dvep',
    'dvm',
    'ea',
    'ed',
    'edd',
    'ei',
    'eit',
    'els',
    'emd',
    'emt-b',
    'emt-i/85',
    'emt-i/99',
    'emt-p',
    'enp',
    'erd',
    'esq',
    'evp',
    'faafp',
    'faan',
    'faap',
    'fac-c',
    'facc',
    'facd',
    'facem',
    'facep',
    'facha',
    'facofp',
    'facog',
    'facp',
    'facph',
    'facs',
    'faia',
    'faicp',
    'fala',
    'fashp',
    'fasid',
    'fasla',
    'fasma',
    'faspen',
    'fca',
    'fcas',
    'fcela',
    'fd',
    'fec',
    'fhames',
    'fic',
    'ficf',
    'fieee',
    'fmp',
    'fmva',
    'fnss',
    'fp&a',
    'fp-c',
    'fpc',
    'frm',
    'fsa',
    'fsdp',
    'fws',
    'gaee[14]',
    'gba',
    'gbe',
    'gc',
    'gcb',
    'gcb',
    'gchs',
    'gcie',
    'gcmg',
    'gcmg',
    'gcsi',
    'gcvo',
    'gcvo',
    'gisp',
    'git',
    'gm',
    'gmb',
    'gmr',
    'gphr',
    'gri',
    'grp',
    'gsmieee',
    'hccp',
    'hrs',
    'iaccp',
    'iaee',
    'iccm-d',
    'iccm-f',
    'idsm',
    'ifgict',
    'iom',
    'ipep',
    'ipm',
    'iso',
    'issp-csp',
    'issp-sa',
    'itil',
    'jd',
    'jp',
    'kbe',
    'kcb',
    'kchs/dchs',
    'kcie',
    'kcie',
    'kcmg',
    'kcsi',
    'kcsi',
    'kcvo',
    'kg',
    'khs/dhs',
    'kp',
    'kt',
    'lac',
    'lcmt',
    'lcpc',
    'lcsw',
    'leed ap',
    'lg',
    'litk',
    'litl',
    'litp',
    'llm',
    'lm',
    'lmsw',
    'lmt',
    'lp',
    'lpa',
    'lpc',
    'lpn',
    'lpss',
    'lsi',
    'lsit',
    'lt',
    'lvn',
    'lvo',
    'lvt',
    'ma',
    'maaa',
    'mai',
    'mba',
    'mbe',
    'mbs',
    'mc',
    'mcct',
    'mcdba',
    'mches',
    'mcm',
    'mcp',
    'mcpd',
    'mcsa',
    'mcsd',
    'mcse',
    'mct',
    'md',
    'mdiv',
    'mem',
    'mfa',
    'micp',
    'mieee',
    'mirm',
    'mle',
    'mls',
    'mlse',
    'mlt',
    'mm',
    'mmad',
    'mmas',
    'mnaa',
    'mnae',
    'mp',
    'mpa',
    'mph',
    'mpse',
    'mra',
    'ms',
    'msa',
    'msc'
    'mscmsm',
    'msm',
    'mt',
    'mts',
    'mvo',
    'nbc-his',
    'nbcch',
    'nbcch-ps',
    'nbcdch',
    'nbcdch-ps',
    'nbcfch',
    'nbcfch-ps',
    'nbct',
    'ncarb',
    'nccp',
    'ncidq',
    'ncps',
    'ncso',
    'ncto',
    'nd',
    'ndtr',
    'nicet i',
    'nicet ii',
    'nicet iii',
    'nicet iv',
    'nmd',
    'np',
    'np[18]',
    'nraemt',
    'nremr',
    'nremt',
    'nrp',
    'obe',
    'obi',
    'oca',
    'ocm',
    'ocp',
    'od',
    'om',
    'oscp',
    'ot',
    'pa-c',
    'pcc',
    'pci',
    'pe',
    'pfmp',
    'pg',
    'pgmp',
    'ph',
    'pharmd',
    'phc',
    'phd',
    'phr',
    'phrca',
    'pla',
    'pls',
    'pmc',
    'pmi-acp',
    'pmp',
    'pp',
    'pps',
    'prm',
    'psm i',
    'psm ii',
    'psm',
    'psp',
    'psyd',
    'pt',
    'pta',
    'qam',
    'qc',
    'qcsw',
    'qfsm',
    'qgm',
    'qpm',
    'qsd',
    'qsp',
    'ra',
    'rai',
    'rba',
    'rci',
    'rcp',
    'rd',
    'rdcs',
    'rdh',
    'rdms',
    'rdn',
    'res',
    'rfp',
    'rhca',
    'rid',
    'rls',
    'rmsks',
    'rn',
    'rp',
    'rpa',
    'rph',
    'rpl',
    'rrc',
    'rrt',
    'rrt-accs',
    'rrt-nps',
    'rrt-sds',
    'rtrp',
    'rvm',
    'rvt',
    'sa',
    'same',
    'sasm',
    'sccp',
    'scmp',
    'se',
    'secb',
    'sfp',
    'sgm',
    'shrm-cp',
    'shrm-scp',
    'si',
    'siie',
    'smieee',
    'sphr',
    'sra',
    'sscp',
    'stmieee',
    'tbr-ct',
    'td',
    'thd',
    'thm',
    'ud',
    'usa',
    'usaf',
    'usar',
    'uscg',
    'usmc',
    'usn',
    'usnr',
    'uxc',
    'uxmc',
    'vc',
    'vc',
    'vcp',
    'vd',
    'vrd',
])
"""

Post-nominal acronyms. Titles, degrees and other things people stick after their name
that may or may not have periods between the letters. The parser removes periods
when matching against these pieces.

"""
