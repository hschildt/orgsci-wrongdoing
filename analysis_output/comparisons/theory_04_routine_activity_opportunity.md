# Routine activity theory and the opportunity perspective: comparison across cases

*Generated 2026-10-29 by compare_tables.py with eu.anthropic.claude-haiku-4-5-20251001-v1:0, from analysis_output/04_routine_activity_opportunity.csv. Presence: ●●● strong, ●●○ moderate, ●○○ weak, ○○○ absent; n = passages coded. Coverage = presence points ÷ maximum, computed in Python. ⚠ = answer trimmed after failing a rule check.*

## Presence by category

| Category | Boeing 737MAX | Dieselgate | Enron | Ford Pinto | Purdue OxyContin |
|---|---|---|---|---|---|
| Motivated offenders and their positions | ●●● 58 | ●●● 45 | ●●● 51 | ●●● 13 | ●●● 44 |
| Suitable targets | ●●● 67 | ●●● 57 | ●●● 58 | ●●● 18 | ●●● 39 |
| Capable guardians and their capacity | ●●● 56 | ●●● 66 | ●●● 38 | ●●● 26 | ●●○ 26 |
| Weakened, captured or delegated guardianship | ●●● 150 | ●●● 90 | ●●● 101 | ●●● 26 | ●●● 48 |
| Predictable guardian routines | ●●● 36 | ●●● 42 | ●●● 28 | ●●● 11 | ●●● 12 |
| Handlers and place managers (internal controls) | ●●● 99 | ●●● 37 | ●●● 54 | ●●● 9 | ●●● 33 |
| Legitimate access and separation from victims | ●●● 54 | ●●● 38 | ●●● 52 | ●●● 12 | ●●● 39 |
| Superficial legitimacy and concealment | ●●● 99 | ●●● 68 | ●●● 151 | ●●● 14 | ●●● 64 |
| Convergence breaks and detection | ●●● 110 | ●●● 69 | ●●● 84 | ●●● 35 | ●●● 64 |
| **Coverage** | **100%** | **100%** | **100%** | **100%** | **96%** |

Ranking by coverage: Boeing 737MAX (100%) > Dieselgate (100%) > Enron (100%) > Ford Pinto (100%) > Purdue OxyContin (96%)

## Cross-case pattern

Routine activity theory explains all five corporate wrongdoing cases through the convergence of motivated offenders in legitimate positions, suitable targets lacking information or capacity to resist, weakened or captured guardians, and concealment strategies that exploit predictable oversight routines until detection triggers intervention.

| Category | Common pattern | Key difference | Most pronounced | Least pronounced |
|---|---|---|---|---|
| Motivated offenders and their positions | All cases involve senior employees or owners in legitimate authority positions—executives, engineers, managers—who exploit their occupational roles and access to decision-making to pursue wrongdoing motivated by cost savings, profit maximization, or schedule pressures. | Boeing and Ford cases involve technical and operational personnel enforcing wrongdoing through hierarchical authority; Enron involves financial executives using complex structures; Dieselgate involves engineers designing technical deception; Purdue involves family ownership exercising direct control over strategy. | Purdue OxyContin | Dieselgate |
| Suitable targets | All cases involve targets—pilots, passengers, regulators, investors, consumers, patients, prescribers—who lack information, technical capacity, or time to detect wrongdoing and rely on offenders' representations or incomplete data to make decisions. | Boeing and Ford target end-users (pilots, passengers, consumers) who cannot detect physical defects; Dieselgate targets regulators who cannot detect software; Enron targets investors and analysts who cannot detect accounting manipulation; Purdue targets both prescribers and patients with information asymmetries. | Purdue OxyContin | Dieselgate |
| Capable guardians and their capacity | All cases involve regulatory or oversight bodies with formal authority and mandates but insufficient resources, expertise, technical capacity, or independence to detect wrongdoing, relying on manufacturer-supplied data or limited sampling. | Boeing and Dieselgate involve technical regulatory agencies with specific certification mandates but resource constraints; Enron involves multiple guardians (SEC, auditors, rating agencies) with conflicting incentives; Ford involves NHTSA with testing capacity but limited authority; Purdue involves FDA and DEA with moderate capacity constraints. | Boeing 737MAX | Purdue OxyContin |
| Weakened, captured or delegated guardianship | All cases involve guardianship weakened through delegation to offenders, reliance on self-reporting, conflicts of interest, information gaps, or regulatory capture that prevents independent verification and enforcement. | Boeing involves explicit delegation through ODA and organizational fragmentation within FAA; Dieselgate involves reliance on manufacturer testing without verification; Enron involves auditor conflicts and board delegation; Ford involves industry influence on regulatory frameworks; Purdue involves data manipulation and advocacy group capture. | Boeing 737MAX | Enron |
| Predictable guardian routines | All cases involve offenders exploiting predictable features of regulatory or oversight processes—standardized testing procedures, reporting deadlines, sampling methods, certification timelines—by timing disclosures, designing deception to match test parameters, or strategically withholding information. | Dieselgate involves technical exploitation of specific test parameters; Boeing involves strategic timing of information submission; Enron involves timing transactions to reporting periods; Ford involves prolonging regulatory processes; Purdue involves avoiding documentation trails and manipulating quota data. | Dieselgate | Ford Pinto |
| Handlers and place managers (internal controls) | All cases involve internal handlers and controls that were present but systematically failed to prevent or stop wrongdoing, either through being overruled, ignored, or complicit in suppressing concerns and evidence. | Boeing and Ford involve supervisors raising concerns that were overruled; Dieselgate involves managers instructing evidence destruction; Enron involves board and audit committee failures to scrutinize; Purdue involves systematic reversal of safeguards and suppression of red flags. | Purdue OxyContin | Dieselgate |
| Legitimate access and separation from victims | All cases involve offenders using legitimate occupational roles and routine business channels to access decision-making, information, or targets, while remaining spatially, temporally, or organizationally distant from victims who cannot observe or verify wrongdoing. | Boeing and Dieselgate involve regulatory submission processes; Enron involves financial management roles; Ford involves design and testing roles; Purdue involves sales representative access to prescribers; all maintain distance between decision-makers and harmed parties. | Purdue OxyContin | Enron |
| Superficial legitimacy and concealment | All cases involve systematic concealment strategies—withholding information, misleading statements, false certifications, document destruction, deceptive framing—that make wrongdoing appear legitimate to regulators, customers, investors, or healthcare providers. | Boeing involves manual removal and selective disclosure; Dieselgate involves false certifications and document destruction; Enron involves complex financial structures and oral side deals; Ford involves misleading analyses; Purdue involves false marketing claims and concealed commercial intent. | Enron | Ford Pinto |
| Convergence breaks and detection | All cases involve detection triggered by external events or new guardians—crashes, independent testing, investigative journalism, whistleblowers, or enforcement actions—that break the convergence of offenders, targets, and weakened guardians. | Boeing and Ford involve physical crashes and accident investigations; Dieselgate involves independent emissions testing; Enron involves multiple detection pathways (journalists, short sellers, whistleblowers, regulators); Purdue involves media reports and law enforcement investigations. | Boeing 737MAX | Purdue OxyContin |

## Category detail

### Motivated offenders and their positions

| Case | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Boeing 737MAX | ●●● strong (n=58, 20 docs) | Boeing employees in technical and management positions (Chief Technical Pilots, Chief Project Engineer, CEO) with authority over design, certification, and communications deliberately concealed MCAS capabilities and design changes from the FAA to secure lower-cost Level B training requirements and maintain production schedules, motivated by cost savings and schedule pressures. | Boeing Employee-1; Boeing Employee-2; Michael Teal; Dennis Muilenburg | November 2016 through December 2018 | E1, E2, E3 |
| Dieselgate | ●●● strong (n=45, 14 docs) | Engineers and managers at VW and Audi, positioned in engine development and quality management, designed and directed the installation of software defeat devices in diesel engines to meet U.S. emissions standards while maintaining performance, deceiving regulators and customers about compliance. | Dorenkamp; Neusser; Pamio; VW AG | 2006 to September 2015 | E4, E5, E6 |
| Enron | ●●● strong (n=51, 15 docs) | Senior executives in high-authority positions—CFO Fastow, CEO Skilling, CAO Causey, and Treasurer Glisan—used their control over financial operations and structured finance to enrich themselves through undisclosed fees, stock sales, and personal investments in special purpose entities while manipulating Enron's reported earnings. | Andrew Fastow, CFO; Jeffrey Skilling, CEO; Richard Causey, CAO; Michael Kopper, Finance | 1997 to October 2001 | E7, E8, E9 |
| Ford Pinto | ●●● strong (n=13, 5 docs) | Lee Iacocca, as executive vice president, ordered the Pinto's accelerated production schedule and enforced strict cost and weight limits that prevented safety improvements, while higher-level management made the decision to proceed with production despite knowing the gas tank was vulnerable to puncture and that feasible fixes existed. | Lee Iacocca; Bob Alexander; Ford management; J.C. Echold | 1968-1972 | E10, E11, E12 |
| Purdue OxyContin | ●●● strong (n=44, 12 docs) | The Sackler family owned and controlled Purdue Pharma, held majority board seats, and exercised direct authority over sales strategies, marketing campaigns, and profit extraction, while employing hundreds of sales representatives to execute their directives to increase opioid prescriptions and sales volumes. | Sackler family; Purdue Pharma; Richard Sackler | 1996 to 2018 | E13, E14, E15 |

### Suitable targets

| Case | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Boeing 737MAX | ●●● strong (n=67, 19 docs) | Pilots and passengers were suitable targets because they lacked information about MCAS and its operational scope, relied on incomplete manuals and training materials, and could not detect the system's activation or malfunction due to absent or inadequate displays and alerts. | Pilots; Passengers; Boeing; FAA AEG | 2017 to 2019 | E16, E17, E18 |
| Dieselgate | ●●● strong (n=57, 15 docs) | Regulators' test procedures and certification processes were vulnerable targets because they relied on standardized laboratory tests with specific, predictable parameters that VW software could detect and exploit, combined with manufacturers' self-testing and regulators' limited independent verification capacity. | VW; EPA; CARB; Regulators | 2006 to 2015 | E19, E20, E21 |
| Enron | ●●● strong (n=58, 16 docs) | Investors, credit rating agencies, and financial analysts were vulnerable targets because they relied on Enron's reported financial information, earnings guidance, and credit ratings to make investment and lending decisions, while Enron's complex accounting manipulations and off-balance-sheet transactions made the true financial condition invisible and undetectable. | Investors; Credit rating agencies; Financial analysts; Enron management | 1997 to 2001 | E22, E23, E24 |
| Ford Pinto | ●●● strong (n=18, 6 docs) | Pinto consumers were suitable targets because the fuel tank was vulnerable to puncture and leakage in rear-end collisions at low speeds (20-30 mph), Ford knew this from crash tests but sold the vehicles without fixing inexpensive defects, and consumers could not detect the defect or the risk they faced. | Ford Motor Co.; Pinto consumers; NHTSA | 1969-1978 | E25, E26, E27 |
| Purdue OxyContin | ●●● strong (n=39, 12 docs) | Purdue identified and targeted high-volume prescribers (top 2% writing 80% of OxyContin prescriptions) and vulnerable patient populations (elderly, veterans, opioid-naive, osteoarthritis patients) as suitable targets because they were responsive to marketing, accessible through sales representatives, and lacked adequate training or time to evaluate risks; patients were further vulnerable due to dependence on prescriber information and reduced out-of-pocket costs through savings cards. | Purdue Pharma; high-volume prescribers; primary care physicians; Sackler family | 1995 to 2019 | E28, E29, E30 |

### Capable guardians and their capacity

| Case | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Boeing 737MAX | ●●● strong (n=56, 20 docs) | The FAA and international regulators possessed formal authority and mandate to certify aircraft and determine pilot training requirements, but lacked sufficient resources, expertise, and independence to detect Boeing's withholding of MCAS information, with only 24 senior engineers overseeing 1,500 Boeing-designated representatives and inspectors reporting insufficient training and concerns that safety issues would not be addressed. | FAA Aircraft Evaluation Group; FAA Seattle BASOO office; Joint Authorities Technical Review | 2014-2020 | E31, E32, E33 |
| Dieselgate | ●●● strong (n=66, 15 docs) | EPA and CARB possessed regulatory authority and mandate to establish emissions standards, certify vehicles, conduct testing and surveillance, and enforce compliance, but lacked sufficient resources, expertise, and technical capacity to detect defeat devices embedded in vehicle software, and relied heavily on manufacturer-supplied test data rather than independent verification. | EPA; CARB; KBA; Umweltbundesamt | 2008-2015 | E34, E35, E36 |
| Enron | ●●● strong (n=38, 15 docs) | External guardians including the SEC, Arthur Andersen auditors, and credit rating agencies had mandates to detect wrongdoing, but faced significant capacity constraints, conflicts of interest, and information limitations that prevented effective oversight of Enron's off-the-books transactions and financial misstatements. | SEC; Arthur Andersen; Moody's; Standard & Poor's | 1997 to 2001 | E37, E38, E39 |
| Ford Pinto | ●●● strong (n=26, 5 docs) | NHTSA conducted compliance testing programs and safety defect investigations that revealed fuel system integrity failures in the Pinto, examined consumer complaints and repair shop data through its Parts Return Program, and made initial defect determinations that could lead to manufacturer recalls. | NHTSA; Joan Claybrook | 1977-1978 | E40, E41, E42 |
| Purdue OxyContin | ●●○ moderate (n=26, 11 docs) | FDA and DEA had regulatory authority and oversight mandates for OxyContin as a Schedule II controlled substance, but FDA lacked sufficient staffing (39 staff for 34,000 promotional materials annually) and could not require pre-approval of promotional materials, while DEA relied on manufacturer-reported data to set production quotas. | FDA; DEA; Department of Health and Human Services | 1996 to 2010 | E43, E44, E45 |

### Weakened, captured or delegated guardianship

| Case | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Boeing 737MAX | ●●● strong (n=150, 20 docs) | The FAA delegated approximately 40% of B737 MAX certification plans to Boeing's ODA; the FAA had inadequate awareness and limited involvement in MCAS certification, preventing independent assessment; Boeing employees withheld critical information about MCAS expansion from the FAA AEG while disclosing it selectively to other FAA personnel, exploiting organizational fragmentation within the FAA. | FAA; Boeing; Boeing ODA; FAA AEG | 2015-2016 | E46, E47, E48 |
| Dieselgate | ●●● strong (n=90, 15 docs) | Guardianship was weakened by reliance on manufacturer-supplied test data without independent verification, gaps in regulatory standards and procedures that did not require disclosure of software or defeat devices, lack of in-house testing capacity and expertise at regulatory authorities, and absence of systematic market surveillance until after 2015. | KBA; EPA; European Commission; Technical Services | 2008-2015 | E49, E50, E51 |
| Enron | ●●● strong (n=101, 16 docs) | Auditors with consulting conflicts failed to discharge audit oversight; regulators lacked follow-up mechanisms; Board delegated oversight to management and outside advisors who failed to disclose critical information; internal controls designed to prevent conflicts were overruled by local partners. | Arthur Andersen; Enron Board; SEC; Enron management | 1999-2001 | E52, E53, E54 |
| Ford Pinto | ●●● strong (n=26, 6 docs) | Ford conducted informal lobbying to establish cost-benefit analysis as the acceptable regulatory framework with federal officials, and regulators lacked technical expertise and relied on industry-supplied data and cost valuations to make safety decisions. | Ford Motor Company; NHTSA; Nixon Transportation Secretaries | 1970s, specifically Nixon-Ford years | E55, E56, E57 |
| Purdue OxyContin | ●●● strong (n=48, 12 docs) | Purdue supplied misleading data to the DEA about prescription volumes while concealing high-volume prescribers, exploited weak FDA oversight by distributing promotional materials without review, and captured advocacy groups through millions in payments to shape opioid-friendly messaging and challenge enforcement actions. | Purdue Pharma; DEA; FDA; Sackler family | 1996-2016 | E58, E59, E60 |

### Predictable guardian routines

| Case | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Boeing 737MAX | ●●● strong (n=36, 14 docs) | Boeing exploited predictable FAA certification routines by limiting MCAS disclosure to avoid triggering higher training requirements, withholding expanded operational scope from regulators during provisional approval, and strategically timing information submission to prevent FAA influence on design decisions. | Boeing; Boeing Employee-1; Boeing Employee-2; FAA AEG | 2015 to 2016 | E61, E62, E63 |
| Dieselgate | ●●● strong (n=42, 13 docs) | VW engineers designed defeat device software to recognize and exploit predictable features of regulatory emissions testing: the standardized test cycles (NEFZ, FTP-75), specific driving patterns, steering wheel angle, vehicle speed, engine duration, barometric pressure, and thermal windows (17-30°C), activating emissions controls only during official testing and disabling them during normal driving. | VW engineers; Dorenkamp; Hadler; Audi employees | 2009-2015 model years; software updates through 2013 | E64, E65, E66 |
| Enron | ●●● strong (n=28, 12 docs) | Enron executives exploited predictable oversight routines by timing transactions to quarter-end and year-end reporting periods, adjusting budget targets after quarter close, and executing sales before financial reporting deadlines to meet analyst expectations while avoiding detection by audit sampling and board review procedures. | Skilling; Causey; Fastow; Board Audit Committee | 1999 to 2001 | E67, E68, E69 |
| Ford Pinto | ●●● strong (n=11, 5 docs) | Ford exploited predictable government oversight routines by deliberately prolonging regulatory processes through sequential arguments and technical delays, filing responses at the last allowed moment, and challenging testing procedures and timelines to defer safety standard implementation. | Ford; NHTSA; Ford lobbyists; Department of Transportation | 1968 to 1972 | E70, E71, E72 |
| Purdue OxyContin | ●●● strong (n=12, 7 docs) | Purdue exploited predictable oversight routines by avoiding email trails to evade discovery, manipulating DEA quota data submissions, timing compliance hotline non-reporting to avoid detection, and targeting high-volume prescribers while monitoring pharmacy dispensing policies and inventory constraints. | Purdue Pharma; Sales representatives; DEA; Sackler family | 2013-2019 | E73, E74, E75 |

### Handlers and place managers (internal controls)

| Case | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Boeing 737MAX | ●●● strong (n=99, 18 docs) | Internal handlers including supervisors, engineers, compliance officers, and board committees were present but largely failed to prevent or stop wrongdoing; supervisors raised concerns about safety and quality issues but were overruled or ignored by management, while compliance functions were absent or ineffective during critical periods, and internal controls failed to detect or stop fraudulent certifications and design decisions. | Scott Campbell, 737 General Manager; Ed Pierson, senior plant supervisor; Boeing senior executives; Global Compliance function | 2014-2019, with remedial measures after 2019 | E76, E77, E78 |
| Dieselgate | ●●● strong (n=37, 7 docs) | Internal managers at VW authorized use of defeat device software despite employee concerns, and when informed of the cheating software, instructed subordinates to destroy evidence of the operation rather than halt the practice. | DORENKAMP; HADLER; GOTTWEIS; NEUSSER | 2006 to April 2013 | E79, E80, E81 |
| Enron | ●●● strong (n=54, 15 docs) | Internal handlers including the Board, Audit Committee, Chief Accounting Officer Causey, and Chief Risk Officer Buy were assigned oversight responsibilities for LJM transactions and related-party controls, but failed to implement effective procedures, conduct adequate scrutiny, or take corrective action when presented with concerns about conflicts of interest. | Board of Directors; Audit Committee; Causey; Buy | 1999 to 2001 | E82, E83, E84 |
| Ford Pinto | ●●● strong (n=9, 4 docs) | Internal supervisors and managers received crash test results showing fuel system defects but failed to act; instead, management suppressed safety concerns, prioritized cost over design changes, and approved production despite known risks through a chain-of-command sign-off process. | Lee Iacocca; Mr. MacDonald; Mr. Alexander; Mr. Kennedy | During Pinto development and production approval | E85, E86, E87 |
| Purdue OxyContin | ●●● strong (n=33, 9 docs) | Internal handlers including the Board, compliance officers, and the ADD Program were present but systematically failed to act on red flags: they received reports of suspicious prescribers, ignored safeguards, continued deploying sales reps to flagged providers, reversed decisions to stop calling on problematic doctors, and suppressed information about high-risk prescribers from insurance companies and authorities. | Board of Directors; Sackler family members; Compliance officers; ADD Program staff | 2001 to 2014 | E88, E89, E90 |

### Legitimate access and separation from victims

| Case | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Boeing 737MAX | ●●● strong (n=54, 19 docs) | Boeing employees in legitimate occupational roles—including senior members of the 737 MAX Flight Technical Team and chief technical pilots—accessed FAA certification processes, provided information to regulators, communicated with airline customers, and submitted design documentation through routine business channels, while remaining spatially and organizationally distant from the pilots and passengers who would operate the aircraft. | Boeing employees; 737 MAX Flight Technical Team; FAA AEG; Airline customers | June 2015 to July 2017 | E91, E92, E93 |
| Dieselgate | ●●● strong (n=38, 13 docs) | VW employees in legitimate occupational roles submitted certification applications to EPA and CARB through routine business processes, while consumers purchasing vehicles were spatially, temporally and socially distant from the decision-making and testing that concealed the defeat devices. | VW GOA Engineering and Environmental Office; EPA; CARB | 2008 to 2015 | E94, E95, E96 |
| Enron | ●●● strong (n=52, 15 docs) | Enron executives and employees used legitimate occupational roles in financial management, accounting, and business operations to access and manipulate assets and financial information, while remaining spatially and organizationally separated from investors and creditors who were harmed by fraudulent transactions. | Fastow; Skilling; Causey; Kopper | 1997 to 2001 | E97, E98, E99 |
| Ford Pinto | ●●● strong (n=12, 5 docs) | Ford engineers and officials accessed the Pinto's fuel system defect through legitimate occupational roles in product design and testing, conducting crash tests and design reviews through normal business processes, while victims were spatially and temporally distant—harmed only after cars left factories and entered public use. | Ford engineers; Ford officials; Vice Presidents Alexander and MacDonald; Iacocca | Before and during Pinto production; defect discovered in pre-production testing | E100, E101, E102 |
| Purdue OxyContin | ●●● strong (n=39, 12 docs) | Purdue sales representatives used legitimate occupational roles to access healthcare providers through routine business activities including in-person detailing visits, speaker training programs, and educational conferences, while remaining spatially and socially distant from patients who were harmed by resulting prescriptions. | Purdue sales representatives; Healthcare providers and pharmacies; Purdue executives | 1996 to 2018 | E103, E104, E105 |

### Superficial legitimacy and concealment

| Case | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Boeing 737MAX | ●●● strong (n=99, 17 docs) | Boeing employees systematically concealed MCAS's expanded operational scope from the FAA by removing references to the system from pilot manuals and training materials, making misleading statements about its limited activation envelope, and withholding information about lower-speed operation to maintain the Level B training determination. | Boeing employees; FAA AEG; Boeing management | 2016-2017 | E106, E107, E108 |
| Dieselgate | ●●● strong (n=68, 14 docs) | VW employees created false certifications to regulators, made misleading technical disclosures, and pursued a strategy of concealing defeat devices while appearing to cooperate, using document destruction and scripted deception to prevent regulators from discovering the illegal software. | VW AG employees and managers; Audi AG employees; EPA and CARB regulators | 2006 to September 2015 | E109, E110, E111 |
| Enron | ●●● strong (n=151, 15 docs) | Enron used complex financial structures, misleading descriptions, technical compliance with accounting rules, oral side deals hidden from documents, backdating, and concealment of true economic substance to make fraudulent transactions appear legitimate to auditors, boards, and investors. | Skilling; Fastow; Causey; Enron executives | 1997-2001 | E112, E113, E114 |
| Ford Pinto | ●●● strong (n=14, 4 docs) | Ford used misleading cost-benefit analyses, false crash-test denials, technical arguments to delay regulatory action, and selective disclosure to make dangerous fuel tank designs appear acceptable to government officials and juries. | Ford Motor Company; J.C. Echold; NHTSA; Department of Transportation | 1970-1978 | E115, E116, E117 |
| Purdue OxyContin | ●●● strong (n=64, 11 docs) | Purdue created misleading marketing materials, false claims about addiction risk, deceptive testimonials, and concealed commercial intent behind neutral-appearing medical standards and educational programs to make wrongdoing appear lawful and legitimate. | Purdue Pharma; Sackler family; sales representatives | 1996 to 2016 | E118, E119, E120 |

### Convergence breaks and detection

| Case | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Boeing 737MAX | ●●● strong (n=110, 20 docs) | Two fatal crashes (Lion Air October 2018, Ethiopian Airlines March 2019) triggered immediate detection by accident investigators, regulators, and government agencies, leading to emergency airworthiness directives, fleet grounding, technical reviews, congressional investigations, and DOJ criminal investigation into Boeing's certification disclosures. | FAA; NTSB; DOJ; House Transportation Committee | October 29, 2018 to March 13, 2019 and beyond | E121, E122, E123 |
| Dieselgate | ●●● strong (n=69, 12 docs) | West Virginia University researchers commissioned by ICCT conducted on-road emissions testing in May 2014 that detected NOx emissions 15-35 times above EPA standards, triggering EPA and CARB investigations that led to VW's admission of defeat devices on September 3, 2015, and EPA's Notice of Violation on September 18, 2015. | West Virginia University; ICCT; EPA; CARB | May 2014 to September 18, 2015 | E124, E125, E126 |
| Enron | ●●● strong (n=84, 16 docs) | Multiple new guardians detected wrongdoing: journalists (Bethany McLean, Wall Street Journal) questioned Enron's finances starting March 2001; short seller James Chanos identified problems in late 2000 and tipped off reporters; whistleblower Sherron Watkins alerted management in August 2001; SEC opened inquiries in October 2001; credit rating agencies downgraded Enron in late October and November 2001, triggering cascading revelations and bankruptcy. | Bethany McLean, Fortune reporter; James Chanos, short seller; Sherron Watkins, whistleblower; SEC | March 2001 to November 2001 | E127, E128, E129 |
| Ford Pinto | ●●● strong (n=35, 5 docs) | Multiple guardians detected the Pinto's fuel tank vulnerability: accident reconstruction experts identified the defect pattern in rear-end collisions and encouraged lawyers to pursue manufacturers; NHTSA initiated formal crash testing investigations after consumer complaints; Mother Jones journalists obtained confidential Ford cost-benefit analysis; and juries ruled against Ford in liability suits. | NHTSA; Mother Jones journalists; Accident reconstruction experts; Plaintiffs' lawyers | 1977-1978 | E130, E131, E132 |
| Purdue OxyContin | ●●● strong (n=64, 12 docs) | Media reports, law enforcement investigations, FDA warnings, DEA enforcement actions, and civil litigation exposed OxyContin abuse and diversion starting in 2000, prompting regulatory changes and criminal prosecution of Purdue and its executives in 2007, followed by state lawsuits and bankruptcy in 2019. | DEA; FDA; law enforcement; state attorneys general | 2000 to 2019 | E133, E134, E135 |

## Evidence

**E1.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 51 ≈

> From at least in and around November 2016 through at least in and around December 2018, in the Northern District of Texas and elsewhere, Boeing, through Boeing Employee-1 and Boeing Employee-2, knowingly, and with intent to defraud, conspired to defraud the FAA AEG. At all times during the conspiracy, Boeing Employee-1 and Boeing Employee-2 were acting within the scope of their employment and with the intention, at least in part, to benefit Boeing.

**E2.** Boeing 737MAX, *Boeing_DPA_incl_Statement_of_Facts_2021-01-07*, p. 31

> Boeing Employee-1 and Boeing Employee-2 understood that the FAA AEG relied on them, as members of Boeing's 737 MAX Flight Technical Team, to identify and provide to the FAA AEG all information that was relevant to the FAA AEG in connection with the FAA AEG's publication of the 737 MAX FSB Report, including information that could impact the FAA AEG's differences-training determination.

**E3.** Boeing 737MAX, *Court_Order_Crime_Victims_Rights_Act_2022-10-21*, p. 4

> The Government alleges that two Boeing employees hid MCAS's low-speed expansion from the AEG. Both employees held the position of chief technical pilot for the 737 MAX program at different times. Part of the chief technical pilot's duties were to work with the AEG on the differences training level determination. According to the Government, the chief technical pilots intentionally hid MCAS's low-speed expansion from the AEG so that they could secure the less rigorous—and less expensive—Level B t…

**E4.** Dieselgate, *Pamio_Complaint_2017*, p. 6

> PAMIO and his co-conspirators, however, realized they could not calibrate a diesel engine that would meet NOx emissions standards within the design constraints imposed by other departments at the company. In order to nevertheless market and sell vehicles with the Audi diesel engine in the United States, PAMIO and his co-conspirators directed Audi employees to design and implement software functions to cheat the standard U.S. emissions tests, and then deliberately failed to disclose the software …

**E5.** Dieselgate, *Dorenkamp_et_al_Second_Superseding_Indictment*, p. 8 ≈

> From in or about 2006 until in or about December 2012, DORENKAMP led a team of engineers that developed the diesel engine (the "EA 189" engine) that was designed to meet the new, tougher emissions standards for diesel vehicles in the United States.

**E6.** Dieselgate, *Winterkorn_et_al_Fifth_Superseding_Indictment*, p. 14 ≈

> In at least in or about 2006, VW employees working under the supervision of DORENKAMP and HADLER were designing the new EA 189 2.0 liter diesel engine (later known as the Generation 1 or "Gen 1") that would be the cornerstone of a new project to sell passenger diesel vehicles in the United States. Selling diesel vehicles in the U.S. market was an important strategic goal of VW AG. This project became known within VW as the "US'07" project.

**E7.** Enron, *Fastow_Complaint_Affidavit_2002*, p. 3

> FASTOW was Enron's Chief Financial Officer ("CFO") from March 1998 until October 24, 2001. As CFO, FASTOW was responsible for overseeing many of Enron's financial activities. FASTOW reported directly to Enron's Chief Executive Officer ("CEO").

**E8.** Enron, *Fastow_Superseding_Information*, p. 2

> The defendant ANDREW S. FASTOW, a resident of Houston, Texas, was Enron's Chief Financial Officer from March 1998 until his termination for cause on October 24, 2001. Prior to serving as CFO, FASTOW served as a Managing Director at Enron. As CFO, FASTOW had oversight over many of Enron's financial activities. FASTOW reported directly to Enron's Chief Executive Officer ("CEO"). During the time that he served as Enron's CFO, FASTOW also served as the general partner and otherwise was in control of…

**E9.** Enron, *Skilling_Lay_Causey_Superseding_Indictment*, p. 3 ≈

> In January 1997, Enron promoted SKILLING to President and Chief Operating Officer ("COO") of the entire company, reporting directly to Enron's CEO and Chairman. In February 2001, SKILLING was named President and CEO of Enron. As COO and CEO of Enron, SKILLING was the senior manager of the company's commercial operations and finances and one of its principal spokespersons with the investing public. SKILLING closely supervised on a day-to-day basis the activities of each of Enron's business units …

**E10.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> Like the Mustang, the Pinto became known in the company as "Lee's car." Lee Iococca wanted that little car in the showrooms of America with the 1971 models. So he ordered his engineering vice president, Bob Alexander, to oversee what was probably the shortest production planning period in modern automotive history. The normal time span from conception to production of a new car model is about 43 months. The Pinto schedule was set at just under 25.

**E11.** Ford Pinto, *Grimshaw_v_Ford_Motor_Co_1981_CalCtApp_119CalApp3d757*, p. 777 ≈

> Harley Copp, a former Ford engineer and executive in charge of the crash testing program, testified that the highest level of Ford's management made the decision to go forward with the production of the Pinto, knowing that the gas tank was vulnerable to puncture and rupture at low rear impact speeds creating a significant risk of death or injury from fire and knowing that 'fixes' were feasible at nominal cost. He testified that management's decision was based on the cost savings which would inur…

**E12.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> Heightening the anti-safety pressure on Pinto engineers was an important goal set by Iacocca known as "the limits of 2,000." The Pinto was not to weigh an ounce over 2,000 pounds and not to cost a cent over $2,000. "Iacocca enforced these limits with an iron hand," recalls the engineer quoted earlier. So, even when a crash test showed that that one-pound, one-dollar piece of plastic stopped the puncture of the gas tank, it was thrown out as extra cost and extra weight.

**E13.** Purdue OxyContin, *Massachusetts_AG_First_Amended_Complaint_Purdue_Sacklers_2019-01-31*, p. 54

> The Sackler family owns Purdue, and they always held a majority of the seats on its Board. Because they controlled their own privately held drug company, the Sacklers had the power to decide how addictive narcotics were sold. They hired hundreds of workers to carry out their wishes, and they fired those who didn't sell enough drugs.

**E14.** Purdue OxyContin, *SCOTUS_Harrington_v_Purdue_Pharma_Opinion_2024-06-27*, p. 6 ≈

> Purdue was a "family company," owned and controlled by the Sacklers. Members of the Sackler family served as president and chief executive officer; they dominated the board of directors; and they "were heavily involved" in the firm's marketing strategies. They "pushed sales targets," too, and "accompanied sales representatives on 'ride along' visits to health care providers" in an effort to maximize OxyContin sales.

**E15.** Purdue OxyContin, *DOJ_Purdue_Civil_Settlement_Agreement_2020-10*, p. 34

> By virtue of OxyContin's importance, certain of the Sacklers placed pressure on executives to meet OxyContin sales goals set by the Board and participated in decision-making regarding Purdue's sales strategies for OxyContin, at times overruling the targets set by Purdue's executives.

**E16.** Boeing 737MAX, *Boeing_DPA_incl_Statement_of_Facts_2021-01-07*, p. 41 ≈

> Because of Boeing's intentional withholding of information from the FAA AEG, the final version of the 737 MAX FSB Report lacked information about MCAS, and relevant portions of this 737 MAX FSB Report were materially false, inaccurate, and incomplete. In turn, airplane manuals and pilot-training materials for U.S.-based airlines lacked information about MCAS, and relevant portions of these manuals and materials were similarly materially false, inaccurate, and incomplete as a result. After the FA…

**E17.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 125

> The unions representing pilots at American Airlines and Southwest Airlines, both of which operate the 737 MAX, allege their members were not made aware of MCAS and the system's ability to command the 737 MAX into a dive until after the Lion Air crash. Captain Dan Carey, then-President of the Allied Pilots Association, which represents American Airlines pilots, testified before the Subcommittee on Aviation in June 2019 that, "[t]he huge error of omission was the fact that Boeing failed to disclos…

**E18.** Boeing 737MAX, *House_TI_Hearing_FAA_Oversight_Pierson_testimony_2019-12-11*, p. 127

> The pilots had no previous knowledge of MCAS and the aircraft provided no displays to indicate that MCAS was acting on the aircraft trim, nor any displays to help them understand that it was getting erroneous data. They were in the dark regarding the functioning of MCAS in these accidents.

**E19.** Dieselgate, *Pamio_Complaint_2017*, p. 17 ≈

> while designing and implementing the defeat devices, PAMIO and his co-conspirators knew that U.S. regulators would measure Audi's diesel vehicles' emissions through standard tests with specific, published drive cycles. Audi employees designed the Audi defeat devices to recognize whether the vehicle was undergoing standard U.S. emissions testing on a dynamometer (or "dyno") or whether the vehicle was being driven on the road.

**E20.** Dieselgate, *DOJ_EPA_Amended_Civil_Complaint_2016*, p. 17 ≈

> The EDC17 ECM of the 2.0L Subject Vehicles contains software functions and/or calibrations that sense when the vehicle is being tested for compliance with applicable emission standards, based on various inputs including the position of the steering wheel, vehicle speed, the duration of the engine's operation, and barometric pressure. These inputs precisely track the parameters of the federal test procedure ('FTP') and other test cycles used for emission testing required to obtain a COC.

**E21.** Dieselgate, *Dorenkamp_et_al_Second_Superseding_Indictment*, p. 14 ≈

> DORENKAMP, HADLER, and their co-conspirators, however, realized that they could not design a diesel engine that would both meet the stricter NOx emissions standards that would become effective in 2007 and attract sufficient customer demand in the U.S. market. Instead of bringing to market a diesel vehicle that could legitimately meet the new, more restrictive U.S. NOx emissions standards, VW employees acting at the direction of DORENKAMP, HADLER, and their co-conspirators, designed, created, and…

**E22.** Enron, *SEC_Complaint_Skilling_Causey_2004*

> Because it was a public company, Enron and its directors, officers, and employees were required to comply with federal securities laws, including rules and regulations requiring the filing of true and accurate financial information. Enron's stock price was influenced by factors such as its reported financial information, credit rating, and its ability to meet revenue and earnings targets and forecasts. Investors considered this information important in making investment decisions. Likewise, the …

**E23.** Enron, *Causey_Indictment_2004*, p. 2

> The price of Enron's stock was influenced by factors such as Enron's reported revenue, earnings, debt, cash flow (sometimes categorized as "funds flow"), and credit rating, as well as its ability to meet revenue and earnings targets and forecasts. Enron's management, like that of many public companies, provided guidance to the investing public regarding anticipated revenue and earnings for upcoming reporting periods. Relying in part on the company's guidance, many professional securities analyst…

**E24.** Enron, *Skilling_Lay_Causey_Superseding_Indictment*, p. 2 ≈

> The price of Enron's stock was influenced by factors such as Enron's reported revenue, earnings, debt, cash flow, and credit rating, as well as its growth potential and ability to meet consistently revenue and earnings targets and forecasts. Enron's management provided guidance to the investing public regarding anticipated revenue and earnings for upcoming reporting periods. Such guidance was communicated in presentations and conference calls to securities analysts and in other public statements…

**E25.** Ford Pinto, *Grimshaw_v_Ford_Motor_Co_1981_CalCtApp_119CalApp3d757*, p. 819 ≈

> Through the results of the crash tests Ford knew that the Pinto's fuel tank and rear structure would expose consumers to serious injury or death in a 20- to 30-mile-per-hour collision. Unlike malicious conduct directed toward a single specific individual, Ford's tortious conduct endangered the lives of thousands of Pinto purchasers.

**E26.** Ford Pinto, *Grimshaw_v_Ford_Motor_Co_1981_CalCtApp_119CalApp3d757*, p. 776 ≈

> The vulnerability of the production Pinto's fuel tank at speeds of 20 and 30-miles-per-hour fixed barrier tests could have been remedied by inexpensive 'fixes,' but Ford produced and sold the Pinto to the public without doing anything to remedy the defects.

**E27.** Ford Pinto, *NHTSA_recall_records_Pinto_Bobcat_incl_78V143000*

> IN THE EVENT THE VEHICLE IS STRUCK FROM THE REAR, THE FUEL FILLER PIPE COULD DISCONNECT FROM THE TANK OR THE TANK COULD BE PUNCTURED IN THE FORWARD FACE. THIS WOULD RESULT IN FUEL LEAKAGE.

**E28.** Purdue OxyContin, *Purdue_Criminal_Information_DNJ_2020-11-24*, p. 6 ≈

> PURDUE PHARMA directed its sales representatives to repeatedly visit the most prolific Prescribers of its opioid products and encourage those Prescribers to prescribe increased numbers of PURDUE PHARMA opioid products. PURDUE PHARMA adopted this marketing strategy, in part, because it knew that the top 2 percent of opioid Prescribers wrote close to 80 percent of OxyContin prescriptions nationwide. PURDUE PHARMA identified these highest-prescribing Prescribers as 'Super Core' and 'Core' prescribe…

**E29.** Purdue OxyContin, *DOJ_Purdue_Civil_Settlement_Agreement_2020-10*, p. 31

> Purdue knew, at that time, that the three highest deciles of prescribers combined accounted for only 1.5% of all opioid prescribers nationwide, but wrote 80% of all OxyContin prescriptions nationwide. Purdue also knew that these prescribers were the most responsive to Purdue's detailing.

**E30.** Purdue OxyContin, *Massachusetts_AG_First_Amended_Complaint_Purdue_Sacklers_2019-01-31*, p. 16

> To expand the market for opioids, Purdue also trained sales reps to target vulnerable populations and encourage doctors to put them on opioids, without disclosing the risks. In Massachusetts, Purdue deceptively promoted opioids for elderly patients, veterans, patients who had never taken opioids, and patients with osteoarthritis — putting thousands more patients at risk.

**E31.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 72 ≈

> In October 2019, the Joint Authorities Technical Review (JATR) commissioned by the FAA to review the 737 MAX certification process reported that the Seattle-based Boeing Aviation Safety Oversight Office (BASOO), under the AIR Systems Oversight Division, was comprised of 45 FAA employees, including 24 total engineers, only 6 of whom were senior engineers, who overseeing the 1,500 Boeing-designated ODA unit members, or authorized representatives.

**E32.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 72 ≈

> The allocated staffing levels of 24 BASOO engineers may not be sufficient to carry out the work associated with retained items and with the conduct of oversight duties. There may be a lack of capacity and depth of experience of BASOO engineering members to approve and make findings of compliance for retained items. Depending on the number of entry-level engineers in the BASOO, there could be an imbalance of working-level engineers in relation to the number of senior engineers reasonably expected…

**E33.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 76

> Within AVS overall, 52 percent did not believe they had enough resources and manpower dedicated to safety, 49 percent believed that safety concerns/incidents will not be addressed so they don't report them, and 43 percent do not believe the FAA appropriately delegates certification activities to organizational and individual designees.

**E34.** Dieselgate, *House_EC_Majority_Staff_Hearing_Memo_2015-10-06*, p. 4

> EPA's Office of Transportation and Air Quality (OTAQ) oversees a broad set of compliance activities to ensure that vehicles manufacturers satisfy regulatory requirements. These include the review of COC applications and a variety of testing and other requirements that occur over the life a vehicle. In addition to review of manufacturer supplied testing data, EPA's own testing may include so-called "confirmatory testing," both random and targeted, and in use compliance testing. In addition, OTAQ …

**E35.** Dieselgate, *Bundestag_Abgas_Untersuchungsausschuss_Report_Drs18-12900_2017_DE*, p. 585 ≈

> Heute scheint man im für die Typgenehmigung verantwortlichen Kraftfahrt-Bundesamt (KBA) erkannt zu haben, dass beim Prüfverfahren moderner Fahrzeuge die Unterstützung von IT-Spezialisten hilfreich sein kann. Aber dieser Erkenntnisprozess, den der amtierende KBA-Präsident und Zeuge Ekhard Zinke bei seiner Aussage vor dem Untersuchungsausschuss als persönliche Lernkurve bezeichnete, erfolgte erst lange nachdem der Abgasskandal durch die Aufdeckungen in den USA in den Fokus des öffentlichen Interes…

**E36.** Dieselgate, *Bundestag_Abgas_Untersuchungsausschuss_Report_Drs18-12900_2017_DE*, p. 616 ≈

> Der Sachverständige Prof. Dr. Stefan Hausberger hat darauf hingedeutet, dass auch das Ungleichgewicht zwischen Industrievertretern und Fachbeamten und unzureichende personelle Ressourcen beim Gesetzgeber dazu beigetragen haben: Und wenn das halt dann zwei Beamte anschauen und auf der anderen Seite halt - Industrie 20 Leute mit sehr viel Geld auch Daten bringen, die nicht einmal manipuliert sind - - Also, ich war dabei. Also, die bringen auch vernünftige Daten; aber dann kommt so eine Menge an Ar…

**E37.** Enron, *Senate_Financial_Oversight_of_Enron_SEC_Watchdogs_2002*, p. 12 ≈

> The SEC's Division of Corporation Finance employs approximately 330 people, of whom approximately 144 are lawyers and 107 are accountants; together, they are charged with reviewing the public filings of more than 17,000 public companies in the United States. The Division's staff is organized into 11 groups, with each group responsible for reviewing the filings of a different industry category. The Corporation Finance Division does not have the resources to review every filing submitted; accordin…

**E38.** Enron, *Senate_Financial_Oversight_of_Enron_SEC_Watchdogs_2002*, p. 15

> To look behind the numbers of all the filings SEC staff reviews is too resource-intensive; as further explained below, the SEC relies on auditors to perform this function.

**E39.** Enron, *Healy_Palepu_2003_The_Fall_of_Enron_JEP*, p. 13

> Enron's auditor, Arthur Andersen, has been accused of applying lax standards in their audits because of a conflict of interest over the significant consulting fees generated by Enron. In 2000, Arthur Andersen earned $25 million in audit fees and $27 million in consulting fees. It is difficult to determine whether Andersen's audit problems at Enron arose from the financial incentives to retain the company as a consulting client, as an audit client or both. However, the size of the audit fee alone…

**E40.** Ford Pinto, *NHTSA_News_Releases_Aug-Dec_1977*, p. 46 ≈

> Joan Claybrook, administrator of the department's National Highway Traffic Safety Administration (NHTSA) said that 'the recall is the direct result of our compliance testing program which revealed that this model failed to pass the requirements of federal motor vehicle safety standard No.301-75, Fuel System Integrity.' She said that a 1977, two-door, base model Granada was subjected to a rear impact crash test followed by a static rollover test, and that during the rollover test fluid spillage f…

**E41.** Ford Pinto, *NHTSA_News_Releases_Aug-Dec_1977*, p. 48 ≈

> Because automobile fires are among the most terrifying safety hazards anyone can encounter, we intend to pursue this matter quickly. We will find out whether a safety defect exists, and if so, what we can do to correct it. Ms. Claybrook noted that the millions of people who drive or ride in subcompact cars have a right to know if they are being subjected to an undue risk of fire in rear-end collisions.

**E42.** Ford Pinto, *NHTSA_News_Releases_Jul-Dec_1978*, p. 17

> During this reporting period, 12 new safety-related defect investigations were opened and four were terminated after the manufacturer initiated recall action. At the end of the reporting period, 73 safety-related defect investigations were in progress, including two which are currently in litigation. For terminated cases, information collected during investigations is available for public viewing in the Technical Reference Division, Room 5108, National Highway Traffic Safety Administration, 400 …

**E43.** Purdue OxyContin, *VanZee_2009_Promotion_and_Marketing_of_OxyContin_AJPH*, p. 4

> The FDA has a limited number of staff for overseeing the enormous amount of promotional materials. In 2002, for example, 39 FDA staff members were responsible for reviewing roughly 34 000 pieces of promotional materials.

**E44.** Purdue OxyContin, *GAO-04-110_OxyContin_Abuse_and_Diversion_2003*, p. 17 ≈

> In fiscal year 2002, FDA had 39 staff positions dedicated to oversight of drug advertising and promotion of all pharmaceuticals distributed in the United States. According to FDA, most of the staff focuses on the oversight of promotional communications to physicians. FDA officials told us that in 2001 it received approximately 34,000 pieces of promotional material, including consumer advertisements and promotions to physicians, and received and reviewed 230 complaints about allegedly misleading …

**E45.** Purdue OxyContin, *Purdue_Plea_Agreement_2020-10-20*, p. 16

> The DEA regulates the total quantity of schedule I and II controlled substances that can be manufactured in a given year through a quota system. The quota system provides for the estimated medical, scientific, research, and industrial needs of the United States, for lawful export requirements, and for the establishment and maintenance of reserve stocks, while avoiding overproduction, shortages, and diversion. To determine the annual legitimate need and set appropriate quotas, the DEA relies upon…

**E46.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 73

> The FAA initially delegated acceptance of approximately 40% of the B737 MAX project's certification plans to the Boeing ODA. Additional certification plans that were originally retained for acceptance by the FAA were later delegated to the Boeing ODA as the certification project progressed. While the JATR team did not conduct an exhaustive review of other ODAs, the team observed that delegating the acceptance of certification plans does not appear to be a widespread practice for the FAA.

**E47.** Boeing 737MAX, *JATR_Joint_Authorities_Technical_Review_2019-10*, p. 13

> The BASOO delegated a high percentage of approvals and findings of compliance to the Boeing ODA for the B737 MAX program. With adequate FAA engagement and oversight, the extent of delegation does not in itself compromise safety. However, in the B737 MAX program, the FAA had inadequate awareness of the MCAS function which, coupled with limited involvement, resulted in an inability of the FAA to provide an independent assessment of the adequacy of the Boeing proposed certification activities assoc…

**E48.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 57

> Despite knowing that the FAA AEG had issued its provisional "Level B" determination without any awareness that MCAS's operational scope had been expanded to include high angle of attack conditions in nearly the entire speed range of ordinary commercial flight, Boeing Employee-1 and Boeing Employee-2 did not correct the FAA AEG's understanding of MCAS's operational scope or otherwise ensure that the FAA AEG's "Level B" determination was based on an accurate understanding of MCAS's operation. Inst…

**E49.** Dieselgate, *Bundestag_Abgas_Untersuchungsausschuss_Report_Drs18-12900_2017_DE*, p. 515

> Das Kraftfahrt-Bundesamt prüft fortlaufend im Rahmen von Konformitätsprüfungen (CoP-P-Prüfungen), ob und wie die Fahrzeughersteller ihrer gesetzlichen Selbstverpflichtung nachkommen. Hierbei setzt das Kraftfahrt-Bundesamt grundsätzlich auf der Prüfdokumentation des Herstellers auf. Sofern sich die Informationen oder die Übereinstimmung als unzureichend herausstellen, erfolgt eine Kontrolle des Qualitätsmanagements beim Hersteller (CoP-Q) sowie ggf. ergänzende produktbezogene Überprüfungen.

**E50.** Dieselgate, *Bundestag_Abgas_Untersuchungsausschuss_Report_Drs18-12900_2017_DE*, p. 602

> In Deutschland kümmert sich das Kraftfahrt-Bundesamt aber nicht um diese Aufgabe. Stattdessen testen die Autohersteller selbst, ob ihre Fahrzeuge ordnungsgemäß funktionieren. Tatsächlich prüft das Kraftfahrt-Bundesamt lediglich die Prüfungsunterlagen der Hersteller.

**E51.** Dieselgate, *Bundestag_Abgas_Untersuchungsausschuss_Report_Drs18-12900_2017_DE*, p. 513

> Der Quellcode der Motorsteuerungssoftware sowie die Emissionsminderungsstrategie war mit Blick auf den erforderlichen Schutz von Betriebs- und Geschäftsgeheimnissen in der als Anlage der Richtlinie 2007/46/EG inhaltlich standardisierten Beschreibungsmappe jedoch zu keinem Zeitpunkt genannt und damit vom Hersteller nicht offen zu legen. Zwar eröffnet die Richtlinie 2007/46/EG in Art. 7 Abs. 3 die Möglichkeit, zusätzliche Unterlagen anzufordern, setzt hierfür jedoch eine entsprechende Begründung g…

**E52.** Enron, *Senate_Financial_Oversight_of_Enron_SEC_Watchdogs_2002*, p. 26

> In 2000, Andersen earned $52 million in fees from Enron. Less than half of that amount, $25 million, was for audit work; $27 million related to consulting services. As discussed above, it is difficult to comprehend how such large consulting fees could not have created a serious conflict of interest for Andersen. But regardless of the cause, the result is clear: Enron's auditor failed to discharge its role of verifying the accuracy of Enron's books.

**E53.** Enron, *Healy_Palepu_2003_The_Fall_of_Enron_JEP*, p. 13

> Internal controls at Andersen, designed to protect against conflicted incentives of local partners, failed. For example, Andersen's Houston office, which performed the Enron audit, was permitted to overrule critical reviews of Enron's accounting decisions by Andersen's Practice Partner in Chicago.

**E54.** Enron, *Senate_Financial_Oversight_of_Enron_SEC_Watchdogs_2002*, p. 53

> When SEC staff raises an issue of concern, there appears often to be inadequate follow-up procedures to ensure that the concern is addressed. With respect to the SEC's decision to permit Enron to switch to mark-to-market accounting, we saw that the conditions imposed by Commission staff—that Enron rely on market prices where available and other objective data where not—were in fact the right ones and, had they been followed, the abuses associated with the valuation of Enron's energy contracts mi…

**E55.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> Before the Ford experts left Washington to return to drafting tables in Dearborn they did one other thing. They managed to informally reach an agreement with the major public servants who would be making auto safety decisions. This agreement was that "cost-benefit" would be an acceptable mode of analysis by Detroit and its new regulators. And, as we shall see, cost-benefit analysis quickly became the basis of Ford's argument against safer car design.

**E56.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> Henry headed home to lick his wounds in Grosse Pointe, Michigan, and a planeload of the Ford Motor Company's best brains flew to Washington to start the "education" of the new federal auto safety bureaucrats. Their job was to implant the official industry ideology in the minds of the new officials regulating auto safety. Briefly summarized, that ideology states that auto accidents are caused not by cars, but by 1) people and 2) highway conditions.

**E57.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo* ≈

> All Ford had to do was convince men like John Volpe, Claude Brinegar and William Coleman (successive Secretaries of Transportation during the Nixon-Ford years) that certain safety standards would add so much to the price of cars that fewer people would buy them. This could damage the auto industry, which was still believed to be the bulwark of the American economy. The Nixon Transportation Secretaries were the kind of regulatory officials big business dreams of. They understood and loved capital…

**E58.** Purdue OxyContin, *Purdue_Plea_Agreement_2020-10-20*, p. 16

> To support its requested quota allocation, Purdue provided the DEA with data concerning the quantity and sales volume of prescriptions for Purdue Schedule II controlled substances. Purdue presented these data as constituting the annual medically-related sales of its opioid products, but failed to inform the DEA of over 1.4 million OxyContin prescriptions written by Region Zero HCPs.

**E59.** Purdue OxyContin, *Purdue_Criminal_Information_DNJ_2020-11-24*, p. 11

> Notwithstanding all of the above evidence showing that PURDUE PHARMA was failing to prevent its opioid products from being abused and diverted by problematic Prescribers, PURDUE PHARMA touted the effectiveness of its anti-diversion programs to the DEA. For example, on or about April 12, 2011, a senior member of PURDUE PHARMA's legal department and a senior member of its compliance team met with DEA personnel to discuss PURDUE PHARMA's anti-diversion efforts, including its ADD Program. During the…

**E60.** Purdue OxyContin, *Senate_HSGAC_Fueling_an_Epidemic_Third_Party_Advocacy_Groups_2018*, p. 2 ≈

> The fact that these same manufacturers provided millions of dollars to the groups described below suggests, at the very least, a direct link between corporate donations and the advancement of opioids-friendly messaging. By aligning medical culture with industry goals in this way, many of the groups described in this report may have played a significant role in creating the necessary conditions for the U.S. opioids epidemic.

**E61.** Boeing 737MAX, *Boeing_Non-Prosecution_Agreement_2025-05-29*, p. 29 ≈

> On or about August 16, 2016, before the FAA AEG published the 737 MAX FSB Report, the FAA AEG issued a provisional 'Level B' differences-training determination for the 737 MAX. At the time of this provisional determination, the FAA AEG was unaware that Boeing had expanded MCAS's operational scope. As Boeing Employee-1 and Boeing Employee-2 knew, the FAA AEG based its provisional 'Level B' differences training for the 737 MAX in part on its understanding that MCAS could only activate during the l…

**E62.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 58 ≈

> On or about November 17, 2016, the FAA AEG emailed three Boeing employees, including Boeing Employee-1, Boeing Employee-2, and another Boeing employee, a draft of the forthcoming 737 MAX FSB Report. That same day, Boeing Employee-1 asked Boeing Employee-2 and the other Boeing employee to review the draft 737 MAX FSB Report "for any glaring issues." On or about November 22, 2016, the other Boeing employee emailed the draft 737 MAX FSB Report back to the FAA AEG with proposed edits. Boeing Employe…

**E63.** Boeing 737MAX, *SEC_Order_Boeing_33-11105_2022-09-22*, p. 6

> And in a January 17, 2017 email to the FAA-AEG, Boeing Employee-1 reminded the FAA-AEG to delete any references to MCAS from the FSB Report, saying "Flight Controls: Delete MCAS, recall we decided we weren't going to cover it in the [manuals] or the CBT … since it's way outside the normal operating envelope."

**E64.** Dieselgate, *CRS_R44372_VW_Defeat_Devices_Clean_Air_Act_FAQ_2016*, p. 4

> the software detects when the vehicle is undergoing official compliance testing and activates certain pollution control devices to reduce tailpipe emissions. During normal driving situations, however, the control devices are turned off

**E65.** Dieselgate, *Dorenkamp_et_al_Second_Superseding_Indictment*, p. 15

> If the vehicle's software detected that it was being tested, the vehicle performed in one mode, which satisfied U.S. NOx emissions standards. If the vehicle's software detected that the vehicle was not being tested, it operated in a different mode, in which the effectiveness of the vehicle's emissions control systems was reduced substantially, causing the vehicle to emit substantially higher NOx, sometimes 35 times higher than allowable U.S. standards.

**E66.** Dieselgate, *Dorenkamp_et_al_Second_Superseding_Indictment*, p. 15 ≈

> While employees acting at their direction designed and implemented the defeat device software, DORENKAMP, HADLER, and their co-conspirators knew that U.S. regulators would measure VW's diesel vehicles' emissions through standard tests with specific, published drive cycles. VW employees acting at the direction of DORENKAMP, HADLER, and their co-conspirators designed the VW defeat device to recognize whether the vehicle was undergoing standard U.S. emissions testing on a dynamometer (or "dyno") or…

**E67.** Enron, *Causey_Indictment_2004*, p. 5

> From time to time, CAUSEY and others increased budget targets at or near the end of the quarter, and at times even after the close of the quarter, in order to achieve a revised earnings-per-share objective in comparison to the expectations of equity analysts.

**E68.** Enron, *Skilling_Lay_Causey_Superseding_Indictment*, p. 7 ≈

> From time to time, without regard to the actual performance of the company, defendants JEFFREY K. SKILLING and RICHARD A. CAUSEY and their coconspirators arbitrarily increased budget targets at or near the end of a quarter so that Enron could exceed analysts' expectations by falsely appearing to achieve and publicly reporting a higher than projected earnings-per-share result. At times, SKILLING and CAUSEY caused these revisions to earnings-per-share results even after the close of a quarter, whe…

**E69.** Enron, *SEC_Complaint_Skilling_Causey_2004*

> In the fourth quarter 1999 Enron pushed through several end-of-the-quarter transactions that were designed solely to achieve budget targets at a time when the company was struggling to produce earnings sufficient to ensure that Enron met analysts' predictions for earnings growth. One transaction used by Enron to ensure that its target was met in the fourth quarter of 1999 was a deal, which Skilling, Causey, and others caused to be committed, whereby Enron "sold" Merrill Lynch an interest in elec…

**E70.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> There are several main techniques in the art of combating a government safety standard: a) make your arguments in succession, so the feds can be working on disproving only one at a time; b) claim that the real problem is not X but Y (we already saw one instance of this in "the problem is not cars but people"); c) no matter how ridiculous each argument is, accompany it with thousands of pages of highly technical assertions it will take the government months or, preferably, years to test. Ford's l…

**E71.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> Ford lobbyists then used technique a)—bringing up a new argument. Their line then became: yes, perhaps burn accidents do happen, but rear-end collisions are relatively rare (note the echo of technique b) here as well). Thus Standard 301 was not needed. This set the NHTSA off on a new round of analyzing accident reports. The government's findings finally were that rear-end collisions were seven and a half times more likely to result in fuel spills than were front-end collisions. So much for that …

**E72.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> Waiting, as it normally does, until the last day allowed for response, Ford filed with NHTSA a gargantuan batch of letters, studies and charts now arguing that the federal testing criteria were unfair. Ford also argued that design changes required to meet the standard would take 43 months, which seemed like a rather long time in light of the fact that the entire Pinto was designed in about two years. Specifically, new complaints about the standard involved the weight of the test vehicle, whether…

**E73.** Purdue OxyContin, *Massachusetts_AG_First_Amended_Complaint_Purdue_Sacklers_2019-01-31*, p. 257

> The defendants' unfair and deceptive conduct was well concealed. The defendants deliberately conducted much of their deception through in-person sales visits, in order to avoid a potentially discoverable paper trail. Purdue prohibited its sales reps from emailing doctors. After this Office notified Purdue of our investigation, Purdue changed its decade-old procedure so that sales reps would not write down descriptions of their conversations with doctors for every sales visit, even in Purdue's in…

**E74.** Purdue OxyContin, *Massachusetts_AG_First_Amended_Complaint_Purdue_Sacklers_2019-01-31*, p. 236 ≈

> Purdue's most severe policy against email prohibited sales reps from writing down in emails their sales pitches to doctors. By insisting that sales reps discuss opioids only in face-to-face oral conversations, Purdue tried to avoid discoverable evidence of its misconduct. As the top sales and marketing executive in the company, Gasdia personally enforced that rule with a vengeance. When Gasdia learned that a sales rep had sent a doctor email about Purdue opioids, he ordered: 'Fire her now! We ca…

**E75.** Purdue OxyContin, *Purdue_Plea_Agreement_2020-10-20*, p. 16

> To support its requested quota allocation, Purdue provided the DEA with data concerning the quantity and sales volume of prescriptions for Purdue Schedule II controlled substances.

**E76.** Boeing 737MAX, *House_TI_Hearing_FAA_Oversight_Pierson_testimony_2019-12-11*, p. 79

> To address the worsening factory conditions, I recommended that Boeing ''[s]hut down the production line to allow our team time to regroup so we can safely finish the planes.'' In response, Mr. Campbell assured me that ''safety and quality is number one and schedule come [sic] after that,'' but he did not acknowledge, let alone act on, my recommendation that Boeing shut down the line to allow workers time to safely address the production backlog. Over the following weeks, factory conditions wors…

**E77.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 25 ≈

> In June 2018, Ed Pierson, a senior Boeing plant supervisor at the company's Renton, Washington 737 MAX production factory, emailed Scott Campbell, the 737 General Manager, requesting a meeting about 'safety concerns.' Mr. Pierson described multiple concerns about production and schedule pressures that were impacting quality control and safety issues. 'As a retired Naval Officer and former Squadron Commanding Officer,' wrote Pierson, 'I know how dangerous even the smallest of defects can be to th…

**E78.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 25 ≈

> In July 2018, five weeks after Mr. Pierson's email, he finally met with Mr. Campbell in Mr. Campbell's office. According to Mr. Pierson's testimony to the Committee, he told Mr. Campbell that in the military they would temporarily halt production if they had the kinds of safety problems that Mr. Pierson was seeing on the MAX factory floor. Mr. Campbell allegedly responded: 'The military is not a profit-making organization.' Rather than heeding Mr. Pierson's dire warnings and thoroughly evaluatin…

**E79.** Dieselgate, *Winterkorn_et_al_Fifth_Superseding_Indictment*, p. 15

> Throughout in or around 2006, DORENKAMP authorized VW engineers to use the defeat device in the development of the US '07 project, despite concerns expressed by certain VW AG employees about the propriety of designing and activating the defeat device software.

**E80.** Dieselgate, *Winterkorn_et_al_Fifth_Superseding_Indictment*, p. 19 ≈

> In or around July 2012, engineers from the VW Brand Engine Development department met, in separate meetings, with GOTTWEIS and NEUSSER to explain that they suspected the cause of the hardware failures in the Subject Vehicles was the increased stress on the exhaust system from being driven too long in "dyno" mode as a result of the use of software designed to detect, evade and defeat U.S. emission tests. To illustrate the software's function, the engineers used a document. Although GOTTWEIS and N…

**E81.** Dieselgate, *Dorenkamp_et_al_Second_Superseding_Indictment*, p. 19 ≈

> Although GOTTWEIS and NEUSSER understood the purpose and significance of the software, they each encouraged further concealment of the software. Specifically, GOTTWEIS and NEUSSER each instructed the engineers who presented the issue to them to destroy the document used to illustrate the operation of the cheating software.

**E82.** Enron, *Powers_Report_Special_Investigative_Committee_2002-02-01*, p. 20

> Skilling was Enron's President and Chief Operating Officer, and later its Chief Executive Officer, until his resignation in August 2001. The Board assumed, and properly so, that during the entire period of time covered by the events discussed in this Report, Skilling was sufficiently knowledgeable of and involved in the overall operations of Enron that he would see to it that matters of significance would be brought to the Board's attention. With respect to the LJM partnerships, Skilling persona…

**E83.** Enron, *Powers_Report_Special_Investigative_Committee_2002-02-01*, p. 22

> Buy was and is Enron's Senior Risk Officer. The Board of Directors also charged him with a substantial role in the oversight of Enron's relationship with the LJM partnerships. He was to review and approve all transactions between them. The evidence we have examined suggests that he did not implement a procedure for identifying all LJM1 or LJM2 transactions. Perhaps more importantly, he apparently saw his role as more narrow than the Board had reason to believe, and did not act affirmatively to c…

**E84.** Enron, *Powers_Report_Special_Investigative_Committee_2002-02-01*, p. 21 ≈

> Causey was and is Enron's Chief Accounting Officer. He presided over and participated in a series of accounting judgments that, based on the accounting advice we have received, went well beyond the aggressive. Causey was also charged by the Board of Directors with a substantial role in the oversight of Enron's relationship with the LJM partnerships. He was to review and approve all transactions between Enron and the LJM partnerships, and he was to review those transactions with the Audit and Com…

**E85.** Ford Pinto, *Grimshaw_v_Ford_Motor_Co_1981_CalCtApp_119CalApp3d757*, p. 776 ≈

> During the course of the project, regular product review meetings were held which were chaired by Mr. MacDonald and attended by Mr. Alexander. As the project approached actual production, the engineers responsible for the components of the project 'signed off' to their immediate supervisors who in turn 'signed off' to their superiors and so on up the chain of command until the entire project was approved for public release by Vice Presidents Alexander and MacDonald and ultimately by Mr. Iacocca.…

**E86.** Ford Pinto, *Grimshaw_v_Ford_Motor_Co_1981_CalCtApp_119CalApp3d757*, p. 778

> In these conversations, both men expressed concern about the integrity of the Pinto's fuel system and complained about management's unwillingness to deviate from the design if the change would cost money.

**E87.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> "That person would have been fired. Safety wasn't a popular subject around Ford in those days. With Lee it was taboo. Whenever a problem was raised that meant a delay on the Pinto, Lee would chomp on his cigar, look out the window and say 'Read the product objectives and get back to work.'"

**E88.** Purdue OxyContin, *House_Oversight_Supplemental_Staff_Memo_2020-12-14*, p. 3 ≈

> Documents obtained by DOJ also show that Purdue executives and members of the Sackler family ignored safeguards from the company's Abuse and Diversion Detection program—intended to identify and cut off heath care providers suspected of suspicious prescribing behavior. Although members of the Sackler family were routinely informed of red flags raised by the program, many high-volume prescribers went unreported. Even in cases when they were reported, Purdue continued to deploy sales representative…

**E89.** Purdue OxyContin, *Massachusetts_AG_First_Amended_Complaint_Purdue_Sacklers_2019-01-31*, p. 66 ≈

> Staff told the Sacklers that Purdue received 284 Reports of Concern about abuse and diversion of Purdue's opioids in Q4 2007, and they conducted only 21 field inquiries in response. Staff also reported to the Sacklers that they received 39 tips to Purdue's compliance hotline during the quarter, but Purdue did not report any of them to the authorities. In May, staff told the Sacklers that Purdue had violated its Corporate Integrity Agreement with the U.S. government by failing to supervise its sa…

**E90.** Purdue OxyContin, *Purdue_Criminal_Information_DNJ_2020-11-24*, p. 16 ≈

> On or about November 24, 2014, the senior-level PURDUE PHARMA employee within the ADD Program circulated a memorandum to members of the ADD Program recommending that PURDUE PHARMA sales representatives cease calling on Prescriber-2 and that PURDUE PHARMA refer Prescriber-2 to the DEA for investigation. In response to the memorandum, another senior-level PURDUE PHARMA employee within the ADD Program sent an email to the other members of the ADD Program asking, 'Can we discuss this? My question is…

**E91.** Boeing 737MAX, *SEC_Order_Boeing_33-11105_2022-09-22*, p. 5 ≈

> Boeing employees responsible for communicating with the FAA-AEG as to differences training and manuals certification – including Boeing Employee-1 and Boeing Employee-2, senior members of the 737 MAX Flight Technical Group – presented MCAS to the FAA-AEG as a feature that could only activate in a very specific, high-speed scenario that was outside the normal flight envelope and therefore unlikely to ever be encountered by a commercial pilot. They made these representations to FAA-AEG personnel b…

**E92.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 51 ≈

> Boeing Employee-1 and Boeing Employee-2 understood that the FAA AEG relied on them, as members of Boeing's 737 MAX Flight Technical Team, to identify and provide to the FAA AEG all information that was relevant to the FAA AEG in connection with the FAA AEG's publication of the 737 MAX FSB Report, including information that could impact the FAA AEG's differences-training determination. Boeing Employee-1 and Boeing Employee-2 also understood that, because flight controls were vital to flying moder…

**E93.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 59

> From in or around January 2017 through in or around July 2017 (when the 737 MAX FSB Report was published), Boeing Employee-1 and Boeing Employee-2 sent and caused to be sent emails to representatives of various Boeing airline customers that had agreed to purchase the 737 MAX, including major U.S.-based airlines. In these emails, Boeing Employee-1 and Boeing Employee-2 or members of their 737 MAX Flight Technical Team referenced and included drafts of the forthcoming 737 MAX FSB Report and airpla…

**E94.** Dieselgate, *VW_Third_Superseding_Information_2017*, p. 6

> VW GOA's Engineering and Environmental Office ("EEO") was located in Auburn Hills, Michigan, in the Eastern District of Michigan. Among other things, EEO prepared and submitted applications (the "Applications") for a certificate of conformity and an executive order (collectively, "Certificates") to the EPA and CARB to obtain authorization to sell each of the 2.0 Liter Subject Vehicles and 3.0 Liter Subject Vehicles (collectively, the "Subject Vehicles") in the United States.

**E95.** Dieselgate, *Winterkorn_et_al_Fifth_Superseding_Indictment*, p. 6 ≈

> VW GOA's Engineering and Environmental Office ("EEO") was located in Auburn Hills, Michigan, in the Eastern District of Michigan. Among other things, EEO prepared and submitted applications (the "Applications") for a certificate of conformity and an executive order (collectively, "Certificates") to the EPA and CARB to obtain authorization to sell each of the 2.0 Liter Subject Vehicle, 3.0 Liter Subject Vehicles, and MY 2013-2016 Porsche Cayenne diesel vehicles (the "Porsche Vehicles") (collectiv…

**E96.** Dieselgate, *Dorenkamp_et_al_Second_Superseding_Indictment*, p. 2

> To obtain a certificate of conformity, a manufacturer was required to submit an application to the EPA for each model year and for each test group of vehicles that it intended to sell in the United States. The application was required to be in writing, to be signed by an authorized representative of the manufacturer

**E97.** Enron, *Fastow_Superseding_Information*, p. 2

> As CFO, FASTOW had oversight over many of Enron's financial activities. FASTOW reported directly to Enron's Chief Executive Officer ("CEO"). During the time that he served as Enron's CFO, FASTOW also served as the general partner and otherwise was in control of certain special purpose entities ("SPEs") with which Enron did business.

**E98.** Enron, *Fastow_Complaint_Affidavit_2002*, p. 3

> FASTOW was Enron's Chief Financial Officer ("CFO") from March 1998 until October 24, 2001. As CFO, FASTOW was responsible for overseeing many of Enron's financial activities.

**E99.** Enron, *SEC_Complaint_Fastow_2002* ≈

> Fastow, among others, was responsible for reviewing and verifying the accuracy and reliability of Enron's filings with the Commission, including its year-end financial statements.

**E100.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> Ford engineers discovered in pre-production crash tests that rear-end collisions would rupture the Pinto's fuel system extremely easily. Because assembly-line machinery was already tooled when engineers found this defect, top Ford officials decided to manufacture the car anyway—exploding gas tank and all—even though Ford owned the patent on a much safer gas tank.

**E101.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo* ≈

> This scenario is no news to Ford. Internal company documents in our possession show that Ford has crash-tested the Pinto at a top-secret site more than 40 times and that every test made at over 25 mph without special structural alteration of the car has resulted in a ruptured fuel tank. Despite this, Ford officials denied under oath having crash-tested the Pinto. Eleven of these tests, averaging a 31-mph impact speed, came before Pintos started rolling off the factories.

**E102.** Ford Pinto, *Grimshaw_v_Ford_Motor_Co_1981_CalCtApp_119CalApp3d757*, p. 776 ≈

> During the course of the project, regular product review meetings were held which were chaired by Mr. MacDonald and attended by Mr. Alexander. As the project approached actual production, the engineers responsible for the components of the project 'signed off' to their immediate supervisors who in turn 'signed off' to their superiors and so on up the chain of command until the entire project was approved for public release by Vice Presidents Alexander and MacDonald and ultimately by Mr. Iacocca.

**E103.** Purdue OxyContin, *Massachusetts_AG_First_Amended_Complaint_Purdue_Sacklers_2019-01-31*, p. 11

> Purdue's most powerful tool of deception was sending sales representatives to promote opioids to Massachusetts doctors, nurses, and pharmacists face to face. During sales visits, Purdue reps made false and misleading claims directly to the professionals who care for Massachusetts patients. Purdue assigned reps to specific territories in Massachusetts and gave them lists of Massachusetts doctors to visit. Purdue targeted doctors, nurses, and pharmacists in every part of our Commonwealth.

**E104.** Purdue OxyContin, *DOJ_Purdue_Civil_Settlement_Agreement_2020-10*, p. 29 ≈

> Until it stopped marketing opioids in February 2018, Purdue sought to increase and maintain opioid sales by sending sales representatives to prescribers' offices and pharmacies to meet with prescribers in person; deliver company-developed messaging; give the prescribers meals (such as coffee, breakfast, and lunch) and marketing materials (such as articles, brochures, posters, and other media); and provide information about pharmacies stocking Purdue opioids and prescription coverage, including c…

**E105.** Purdue OxyContin, *GAO-04-110_OxyContin_Abuse_and_Diversion_2003*, p. 25 ≈

> Each Purdue sales representative has a specific sales territory and is responsible for developing a list of about 105 to 140 physicians to call on who already prescribe opioids or who are candidates for prescribing opioids. Each Purdue sales representative is expected to make about 35 physician calls per week and typically calls on each physician every 3 to 4 weeks.

**E106.** Boeing 737MAX, *House_TI_Hearing_FAA_Oversight_Pierson_testimony_2019-12-11*, p. 6

> In fact, during the certification of the 737 MAX, Boeing actively pushed the FAA to remove references to MCAS from the flight crew operating manual, as revealed in the emails and instant messages from Boeing executive Mark Forkner, which Boeing initially failed to provide to the committee. The FAA accepted Boeing's push, and Forkner went on to boast that he was ''Jedi mind-tricking'' other civil aviation regulators around the world to adopt the FAA's faulty decision.

**E107.** Boeing 737MAX, *SEC_Order_Boeing_33-11105_2022-09-22*, p. 6

> Following this exchange, Boeing employees responsible for communicating with the FAA-AEG did not inform the FAA-AEG about the MCAS Expansion. And in a January 17, 2017 email to the FAA-AEG, Boeing Employee-1 reminded the FAA-AEG to delete any references to MCAS from the FSB Report, saying "Flight Controls: Delete MCAS, recall we decided we weren't going to cover it in the [manuals] or the CBT … since it's way outside the normal operating envelope."

**E108.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 57

> For example, shortly after the simulated test flight described in paragraph 30, Boeing Employee-1 talked with FAA AEG Employee-1, who asked Boeing Employee-1 about the simulated test flight. Boeing Employee-1 intentionally withheld and concealed from FAA AEG Employee-1 the fact that MCAS's operational scope had been expanded beyond what the FAA AEG relied upon when it issued its provisional "Level B" differences-training determination for the 737 MAX.

**E109.** Dieselgate, *Winterkorn_et_al_Fifth_Superseding_Indictment*, p. 17 ≈

> As part of the certification process for each new model year, DORENKAMP, NEUSSER, HADLER, GOTTWEIS, PETER, WINTERKORN, and their co-conspirators falsely and fraudulently certified, and/or caused to be certified, to the EPA and CARB that the Subject Vehicles met U.S. emissions standards and complied with standards prescribed by the Clean Air Act. Furthermore, DORENKAMP, NEUSSER, HADLER, GOTTWEIS, PETER, WINTERKORN, and their co-conspirators knew that if they had told the truth and disclosed the e…

**E110.** Dieselgate, *Winterkorn_et_al_Fifth_Superseding_Indictment*, p. 23 ≈

> In response to learning the results of the ICCT study, engineers in the VW Brand Engine Development department formed an ad hoc task force to formulate responses to questions that arose from the U.S. regulators. VW AG employees, including NEUSSER, GOTTWEIS, PETER, WINTERKORN, and their co-conspirators, determined not to disclose to U.S. regulators that the tested vehicle models operated with a defeat device. Instead, NEUSSER, GOTTWEIS, PETER, WINTERKORN, and their co-conspirators pursued a strat…

**E111.** Dieselgate, *Dorenkamp_et_al_Second_Superseding_Indictment*, p. 22 ≈

> In response to learning the results of the ICCT study, engineers in the VW Brand Engine Development department formed an ad hoc task force to formulate responses to questions that arose from the U.S. regulators. VW AG employees, including NEUSSER, GOTTWEIS, SCHMIDT, PETER, and their co-conspirators, determined not to disclose to U.S. regulators that the tested vehicle models operated with a defeat device. Instead, NEUSSER, GOTTWEIS, SCHMIDT, PETER, and their co-conspirators pursued a strategy of…

**E112.** Enron, *House_EC_Hearing_Pt2_Skilling_testimony_2002-02-07*, p. 10

> I think it is epitomized by one little line in the first memo that one of our witnesses, Jordan Mintz, wrote on January 4, and I quote, ''Nicole has advised that if there is a general theme or guideline to follow in the preparation process of all these deals, it is to be as innocuous as possible in terms of description, detail, et cetera.''

**E113.** Enron, *Causey_Indictment_2004*, p. 4

> Enron's executives and senior managers frequently explained the use of these devices to Enron's outside auditors, and at times to the investing public, through misleading descriptions and justifications that were designed to dovetail with accounting and financial reporting requirements but which masked the true intent of Enron''s executives and senior managers to present a false and misleading portrait of Enron's current and likely future financial condition.

**E114.** Enron, *House_EC_Hearing_Pt1_Powers_testimony_2002-02-05*, p. 20 ≈

> The idea of a hedge is normally to contract with a creditworthy outside party that is prepared, for a price, to take on the economic risk of an investment. If the value of the investment goes down, that other party will bear the loss, but that is not what happened here. If you cut through the complexity of these partnerships and transactions, here Enron was essentially hedging with itself. The outside parties with which Enron hedged were the so-called Raptors. The purported outside investor in t…

**E115.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> Not long after the government arrived at the $200,725-per-life figure, it surfaced, rounded off to a cleaner $200,000, in an internal Ford memorandum. This cost-benefit analysis argued that Ford should not make an $11-per-car improvement that would prevent 180 fiery deaths a year. (This minor change would have prevented gas tanks from breaking so easily both in rear-end collisions, like Sandra Gillespie's, and in rollover accidents, where the same thing tends to happen.) Ford's cost-benefit tabl…

**E116.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> But it turns out, on closer examination, that both these findings were misleading. First, note that Ford's table shows an equal number of burn deaths and burn injuries. This is false. All independent experts estimate that for each person who dies by an auto fire, many more are left with charred hands, faces and limbs. Andrew McGuire of the Northern California Burn Center estimates the ratio of burn injuries to deaths at ten to one instead of the one to one Ford shows here. Even though Ford value…

**E117.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> This scenario is no news to Ford. Internal company documents in our possession show that Ford has crash-tested the Pinto at a top-secret site more than 40 times and that every test made at over 25 mph without special structural alteration of the car has resulted in a ruptured fuel tank. Despite this, Ford officials denied under oath having crash-tested the Pinto.

**E118.** Purdue OxyContin, *Senate_Judiciary_Brownlee_Testimony_2007-07-31*, p. 3

> Despite knowing that OxyContin contained high concentrations of oxycodone HCL, had an abuse potential similar to that of morphine, and was at least as addictive as other pain medications on the market, Purdue, beginning in January 1996, marketed and promoted OxyContin as less addictive, less subject to abuse and diversion, and less likely to cause tolerance and withdrawal than other pain medications.

**E119.** Purdue OxyContin, *Senate_Judiciary_Brownlee_Testimony_2007-07-31*, p. 3

> Purdue trained its sales representatives to falsely inform health care providers that it was more difficult to extract the oxycodone from an OxyContin tablet for the purpose of intravenous abuse. Purdue ordered this training even though its own study showed that a drug abuser could extract approximately 68 percent of the oxycodone from a single 10 mg OxyContin tablet by simply crushing the tablet, stirring it in water, and drawing the solution through cotton into a syringe.

**E120.** Purdue OxyContin, *VanZee_2009_Promotion_and_Marketing_of_OxyContin_AJPH*, p. 3 ≈

> Purdue trained its sales representatives to carry the message that the risk of addiction was 'less than one percent'. The company cited studies by Porter and Jick, who found iatrogenic addiction in only 4 of 11882 patients using opioids and by Perry and Heidrich, who found no addiction among 10 000 burn patients treated with opioids. Both of these studies, although shedding some light on the risk of addiction for acute pain, do not help establish the risk of iatrogenic addiction when opioids are…

**E121.** Boeing 737MAX, *FAA_737MAX_Technical_Advisory_Board_Report*, p. 2

> On October 29, 2018, Lion Air flight 610 (JT610), a Boeing Model 737-8 airplane, crashed approximately twelve minutes after takeoff in Jakarta, Indonesia. On March 10, 2019, Ethiopian Airlines flight 302 (ET302), also a Boeing Model 737-8 airplane, crashed approximately six minutes after takeoff in Addis Ababa, Ethiopia. The B737 MAX automated flight control system is an area of interest in both accidents. The FAA determined that the implementation of a Technical Advisory Board (TAB), consisting…

**E122.** Boeing 737MAX, *SEC_Order_Boeing_33-11105_2022-09-22*, p. 2

> On March 13, 2019, three days after the Ethiopian Airlines Crash, the U.S. Federal Aviation Administration ("FAA") issued an order grounding the entire 737 MAX fleet due to ongoing safety concerns; similar grounding orders were issued by regulators around the world. Ultimately, more than 20 months would pass before a 737 MAX was once again permitted to fly.

**E123.** Boeing 737MAX, *JATR_Joint_Authorities_Technical_Review_2019-10*, p. 7

> On October 29, 2018, Lion AIR Flight JT610 (JT610), a B737-8 MAX, crashed shortly after takeoff in Jakarta, Indonesia. On November 7, 2018, the FAA issued Emergency Airworthiness Directive (AD) 2018-23-51 to require revising certificate limitations and operating procedures of the Airplane Flight Manual (AFM) for the B737 MAX to provide the flight crew with runaway horizontal stabilizer trim procedures to follow under certain conditions. On March 10, 2019, Ethiopian Airlines Flight 302 (ET302), a…

**E124.** Dieselgate, *Bundestag_Abgas_Untersuchungsausschuss_Report_Drs18-12900_2017_DE*, p. 32

> Ein von der West Virginia University im Auftrag der ICCT durchgeführter Folgetest in den Vereinigten Staaten führte zum Ergebnis, dass die Stickoxidemissionen von zwei der drei dabei getesteten Fahrzeugen im Realbetrieb deutlich über den amerikanischen Grenzwerten lagen.

**E125.** Dieselgate, *Winterkorn_et_al_Fifth_Superseding_Indictment*, p. 21 ≈

> In or around March 2014, certain VW employees, including NEUSSER, GOTTWEIS, PETER, and WINTERKORN learned of the results of a study undertaken by West Virginia University's Center for Alternative Fuels, Engines and Emissions and commissioned by the International Council on Clean Transportation (the "ICCT study"). The ICCT study identified substantial discrepancies in the NOx emissions from certain 2.0 Liter Subject Vehicles when tested on the road compared to when these vehicles were undergoing …

**E126.** Dieselgate, *CRS_R44372_VW_Defeat_Devices_Clean_Air_Act_FAQ_2016*, p. 5 ≈

> EPA and CARB were alerted to the emissions violations by researchers at West Virginia University (WVU) working under a contract with the International Council on Clean Transportation (ICCT), a nonprofit environmental research organization. As part of a study of on-road emissions from diesel vehicles, the WVU researchers found emissions levels for some vehicles far exceeded U.S. certification standards.

**E127.** Enron, *Senate_Financial_Oversight_of_Enron_SEC_Watchdogs_2002*, p. 90

> On October 17, The Wall Street Journal broke the story about partnerships run by Enron CFO Andrew Fastow being used to hide Enron losses and debt.

**E128.** Enron, *Healy_Palepu_2003_The_Fall_of_Enron_JEP*, p. 14

> By the end of 2000, some dissenting voices were speaking up with regard to Enron. The Economist ("The Energetic Messiah," 2000) questioned Enron's performance, and James Chanos, a hedge fund manager, identified problems from disclosures on related party transactions involving the firm's senior officers and insider trading in late 2000. In November 2000, Chanos shorted the stock, and in February 2001, he tipped off a reporter at Fortune, Bethany McLean, who subsequently wrote the March article "I…

**E129.** Enron, *Healy_Palepu_2003_The_Fall_of_Enron_JEP*, p. 2 ≈

> August 14, 2001: Jeff Skilling resigned as CEO, citing personal reasons. He was replaced by Kenneth Lay. Mid- to late August: Sherron Watkins, an Enron vice president, wrote an anonymous letter to Kenneth Lay expressing concerns about the firm's accounting. She subsequently discussed her concerns with James Hecker, a former colleague and audit partner at Andersen, who contacted the Enron audit team.

**E130.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> While government bureaucrats dragged their feet on lifesaving Standard 301, a different kind of expert was taking a close look at the Pinto—the "recon man." "Recon" stands for reconstruction; recon men reconstruct accidents for police departments, insurance companies and lawyers who want to know exactly who or what caused an accident. It didn't take many rear-end Pinto accidents to demonstrate the weakness of the car. Recon men began encouraging lawyers to look beyond one driver or another to th…

**E131.** Ford Pinto, *NHTSA_News_Releases_Aug-Dec_1977*, p. 48 ≈

> In response to recent charges about the safety of Ford Pinto gas tanks in rear-end collisions, the department's National Highway Traffic Safety Administration (NHTSA) has begun a special program of vehicle-to-vehicle crash testing to measure the susceptibility to fire of fuel tanks in Pintos and other small cars. NHTSA Administrator Joan Claybrook said the agency also will test full sized vehicles to establish a baseline for comparative purposes.

**E132.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> An extensive investigation by Mother Jones over the past six months has found these answers: Fighting strong competition from Volkswagen for the lucrative small-car market, the Ford Motor Company rushed the Pinto into production in much less than the usual time. Ford engineers discovered in pre-production crash tests that rear-end collisions would rupture the Pinto's fuel system extremely easily. Because assembly-line machinery was already tooled when engineers found this defect, top Ford offici…

**E133.** Purdue OxyContin, *GAO-04-110_OxyContin_Abuse_and_Diversion_2003*, p. 7 ≈

> In early 2000, media reports began to surface in several states that OxyContin was being abused—that is, used for nontherapeutic purposes or for purposes other than those for which it was prescribed—and illegally diverted. According to FDA and the Drug Enforcement Administration (DEA), the abuse of OxyContin is associated with serious consequences, including addiction, overdose, and death.

**E134.** Purdue OxyContin, *GAO-04-110_OxyContin_Abuse_and_Diversion_2003*, p. 15

> In response to the abuse and diversion reports, DEA analyzed data collected from medical examiner autopsy reports and crime scene investigation reports. The most recent data available from DEA show that as of February 2002, the agency had verified 146 deaths nationally involving OxyContin in 2000 and 2001.

**E135.** Purdue OxyContin, *Senate_Judiciary_Brownlee_Testimony_2007-07-31*, p. 2

> In response to the effects of OxyContin abuse and diversion, government officials and private citizens began focusing on Purdue and OxyContin. Product liability litigation began in Ohio in April, 2001.
