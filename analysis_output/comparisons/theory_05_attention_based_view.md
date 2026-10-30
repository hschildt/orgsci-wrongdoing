# Attention-based view of the firm: comparison across cases

*Generated 2026-10-29 by compare_tables.py with eu.anthropic.claude-haiku-4-5-20251001-v1:0, from analysis_output/05_attention_based_view.csv. Presence: ●●● strong, ●●○ moderate, ●○○ weak, ○○○ absent; n = passages coded. Coverage = presence points ÷ maximum, computed in Python. ⚠ = answer trimmed after failing a rule check.*

## Presence by category

| Category | Boeing 737MAX | Dieselgate | Enron | Ford Pinto | Purdue OxyContin |
|---|---|---|---|---|---|
| Warning signals and anomalies | ●●● 152 | ●●● 96 | ●●● 81 | ●●● 55 | ●●● 98 |
| Communication and procedural channels | ●●● 108 | ●●● 56 | ●●● 68 | ●●● 17 | ●●● 27 |
| Structural positions and players | ●●● 79 | ●●● 51 | ●●● 71 | ●●● 12 | ●●● 40 |
| Rules of the game and attention-directing incentives | ●●● 79 | ●●● 40 | ●●● 71 | ●●● 13 | ●●● 51 |
| Focus of attention and dominant agendas | ●●● 52 | ●●● 32 | ●●● 52 | ●●● 12 | ●●● 55 |
| Filtering, discounting and neglect of warnings | ●●● 134 | ●●● 61 | ●●● 128 | ●●● 8 | ●●● 58 |
| Organizational responses and moves | ●●● 100 | ●●● 73 | ●●● 71 | ●●● 46 | ●●● 65 |
| Attention shifts and triggering events | ●●● 60 | ●●● 34 | ●●● 46 | ●●● 12 | ●●● 34 |
| **Coverage** | **100%** | **100%** | **100%** | **100%** | **100%** |

Ranking by coverage: Boeing 737MAX (100%) > Dieselgate (100%) > Enron (100%) > Ford Pinto (100%) > Purdue OxyContin (100%)

## Cross-case pattern

Across all five cases, organizational wrongdoing persisted because structural features of attention—communication channels, hierarchical positions, incentive rules, and dominant agendas—systematically filtered, delayed, and prevented warnings from reaching decision-makers or triggering corrective action until external triggering events forced attention shifts.

| Category | Common pattern | Key difference | Most pronounced | Least pronounced |
|---|---|---|---|---|
| Warning signals and anomalies | All cases had strong warning signals from internal actors, external regulators, or both: engineers, whistleblowers, auditors, researchers, and law enforcement detected problems and communicated concerns through various channels. | Boeing and Ford warnings came primarily from internal engineers; Dieselgate and Enron warnings came from both internal and external sources; Purdue warnings came from multiple external parties (pharmacists, law enforcement, medical boards) alongside internal staff. | Enron | Ford Pinto |
| Communication and procedural channels | All cases had formal communication channels designed to surface and address concerns: board processes, audit reviews, regulatory submissions, product review meetings, and internal reporting systems existed in each organization. | Boeing and Enron channels were systematically bypassed through concealment and false representations; Dieselgate channels were deliberately blocked or information was concealed; Ford channels existed but were ineffective due to structural filtering; Purdue channels were often bypassed or rendered ineffective. | Enron | Ford Pinto |
| Structural positions and players | All cases show organizational structures that fragmented attention and created control gaps: hierarchical distance between decision-makers and those with detailed knowledge, compartmentalization across departments or geographic locations, and concentration of authority in positions that benefited from wrongdoing. | Boeing fragmentation was across multiple FAA and Boeing teams; Dieselgate across geographic and hierarchical levels; Enron through dual roles and reporting lines that created conflicts; Ford through vertical hierarchy that filtered information upward; Purdue through family ownership that blurred board-management boundaries. | Enron | Ford Pinto |
| Rules of the game and attention-directing incentives | All cases had formal rules, metrics, and incentive systems that made wrongdoing-related priorities salient while rendering safety, compliance, or ethical concerns invisible to decision-makers. | Boeing and Ford incentives prioritized cost and schedule; Dieselgate incentives made laboratory compliance the only binding metric; Enron incentives tied compensation to stock price and earnings; Purdue incentives tied compensation to sales volume. | Enron | Dieselgate |
| Focus of attention and dominant agendas | All cases show decision-makers focused intensely on metrics that conflicted with safety or compliance: production volume, cost savings, earnings targets, sales revenue, or market success dominated strategy and resource allocation. | Boeing and Ford focused on production and cost; Dieselgate on market success and test compliance; Enron on earnings and stock price; Purdue on sales revenue and profit growth. | Enron | Ford Pinto |
| Filtering, discounting and neglect of warnings | All cases show systematic filtering of warnings through narrowed investigations, reframing of concerns, routing to lower-level officials without authority, incomplete disclosures, and selective information flow that prevented decision-makers from understanding the full scope of problems. | Boeing and Dieselgate involved intentional concealment and false representations to regulators; Enron involved false representations to the board; Ford involved structural filtering that failed to route concerns to decision-makers; Purdue involved high thresholds and reversed decisions that allowed continued wrongdoing. | Boeing 737MAX | Ford Pinto |
| Organizational responses and moves | All cases show organizations responding to warning signals by deferring fixes, concealing evidence, delaying disclosures, and continuing wrongdoing rather than implementing corrective action. | Boeing delayed fixes and misled regulators; Dieselgate concealed defeat devices through false certifications; Enron manipulated financial disclosures; Ford used cost-benefit analysis and lobbying to defer safety improvements; Purdue continued targeting flagged prescribers while concealing evidence. | Dieselgate | Ford Pinto |
| Attention shifts and triggering events | All cases show that organizational attention shifted only after external triggering events—crashes, regulatory violations, media exposés, or lawsuits—redirected focus to the wrongdoing and prompted observable changes in priorities, leadership, and strategic responses. | Boeing and Ford triggering events were crashes and lawsuits; Dieselgate was regulatory violation and public disclosure; Enron was media exposé and SEC investigation; Purdue involved multiple sequential triggering events over years (congressional hearings, DOJ settlement, media exposés). | Boeing 737MAX | Purdue OxyContin |

## Category detail

### Warning signals and anomalies

| Case | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Boeing 737MAX | ●●● strong (n=152, 20 docs) | Boeing engineers predicted in June 2016 that erroneous AOA sensor data could cause adverse MCAS consequences and questioned whether pilots could combat repetitive activation; the FAA issued emergency airworthiness directives in November 2018 after the crashes; whistleblowers reported safety concerns to Congress after the crashes. | Boeing engineers; FAA; NTSB; whistleblowers | June 2016 (pre-crash); November 2018 onwards (post-crash) | E1, E2, E3 |
| Dieselgate | ●●● strong (n=96, 15 docs) | Multiple independent researchers and regulators detected significantly elevated real-world NOx emissions from VW diesel vehicles through on-road testing starting in 2014, while internal VW employees raised concerns about the defeat device design and its detectability as early as 2006-2008. ⚠ | West Virginia University researchers; EPA; CARB; VW engineers | 2006 to September 2015 | E4, E5, E6 |
| Enron | ●●● strong (n=81, 10 docs) | Multiple internal actors—including Sherron Watkins, Jeffrey McMahon, Stuart Zisman, and Enron's risk assessment group—raised concerns about accounting improprieties, conflicts of interest in LJM transactions, Raptor structure risks, and asset valuation problems through memos, meetings, and emails; external auditors Andersen also identified risky accounting practices and conflicts; analysts and journalists questioned financial opacity and business model sustainability; yet these signals were largely ignored or not acted upon by senior management and the Board. | Sherron Watkins; Jeffrey McMahon; Andersen auditors; Bethany McLean | 1999 to August 2001 | E7, E8, E9 |
| Ford Pinto | ●●● strong (n=55, 6 docs) | Ford engineers discovered in pre-production crash tests that the Pinto's fuel system would rupture in rear-end collisions at speeds over 25 mph, and NHTSA received consumer complaints and conducted investigations documenting fatal fires and fuel leakage incidents. | Ford engineers; NHTSA; consumers | 1970-1978 | E10, E11, E12 |
| Purdue OxyContin | ●●● strong (n=98, 12 docs) | Purdue's sales representatives, pharmacists, law enforcement, medical boards, and internal ADD Program staff repeatedly reported concerns about suspicious prescribing patterns, patient deaths, abuse and diversion, and regulatory investigations to Purdue management and the Sackler family, who received these warnings but often continued marketing to flagged prescribers and failed to report findings to authorities. | Purdue sales representatives; Purdue ADD Program; Sackler family; Pharmacists | 2000-2015 | E13, E14, E15 |

### Communication and procedural channels

| Case | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Boeing 737MAX | ●●● strong (n=108, 22 docs) | Information about MCAS was fragmented across multiple certification documents and compartmentalized across different FAA groups and Boeing teams, preventing integrated understanding of the system's full operational scope and safety implications. | Boeing; FAA AEG; FAA BASOO; Boeing Flight Technical Team | 2015-2017 | E16, E17, E18 |
| Dieselgate | ●●● strong (n=56, 13 docs) | Multiple formal channels existed for emissions oversight: EPA and CARB conducted testing and issued certificates of conformity; VW submitted applications with signed certifications; regulators asked increasingly specific questions; steering groups coordinated between German ministries and agencies; and internal VW communications flowed through engineering departments and management, though some channels were deliberately blocked or information was concealed. | EPA; CARB; Volkswagen AG; German ministries and agencies | 2006 to 2015 | E19, E20, E21 |
| Enron | ●●● strong (n=68, 15 docs) | Communication channels including board approval processes, audit committee reviews, and transaction approval checklists were designed but systematically bypassed through false representations to the board, undisclosed side deals, and limited scope investigations that avoided scrutinizing accounting treatment. ⚠ | Board of Directors; Audit Committee; Fastow; Skilling | 1999-2001 | E22, E23, E24 |
| Ford Pinto | ●●● strong (n=17, 5 docs) | Crash test results and safety concerns about the Pinto's fuel tank were forwarded up the chain of command through regular product review meetings where engineers "signed off" to supervisors who signed off to superiors, ultimately reaching Vice Presidents Alexander and MacDonald and Mr. Iacocca for final approval, though a safety engineer's presentation on safer tank design was attended by only two people. | Lou Tubben; MacDonald; Alexander; Iacocca | 1971 through production approval | E25, E26, E27 |
| Purdue OxyContin | ●●● strong (n=27, 10 docs) | Purdue maintained formal reporting channels including Board tracking of sales quotas, an ADD Program with Reports of Concern (ROC) submitted by sales representatives, Region Zero lists for prescribers to cease calling, and weekly sales reports to executives, though these channels were often bypassed or ineffective in stopping high-volume prescribers from receiving continued promotion. | Purdue Board; Sales and Marketing Department; Senior-level employees; Sales representatives | 2002 to February 2018 for ADD Program; 2010-2013 for Board quota tracking | E28, E29, E30 |

### Structural positions and players

| Case | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Boeing 737MAX | ●●● strong (n=79, 21 docs) | Boeing's organizational structure fragmented attention across multiple positions with different responsibilities: the 737 MAX Flight Technical Team withheld MCAS expansion information from the FAA AEG, while other Boeing engineers and senior executives approved MCAS redesigns without full awareness of critical technical details; the FAA's 45-person BASOO office oversaw 1,500 Boeing ODA members with insufficient senior engineers, and separate FAA groups made airworthiness versus training determinations without coordinated information flow. | Boeing 737 MAX Flight Technical Team; FAA AEG; Boeing senior executives; FAA BASOO | 2012-2019 | E31, E32, E33 |
| Dieselgate | ●●● strong (n=51, 12 docs) | VW's organizational structure separated decision-making authority across hierarchical levels and geographic locations: engineers in Wolfsburg developed defeat device software; managers authorized its use; US-based EEO staff submitted certifications to EPA/CARB; and CEO Winterkorn held ultimate authority with Neusser reporting directly to him from 2013-2015. | Winterkorn (CEO); Neusser (head of development); Hadler (engine development); Dorenkamp (after-treatment) | 2003-2015 | E34, E35, E36 |
| Enron | ●●● strong (n=71, 17 docs) | Fastow as CFO controlled both sides of related-party transactions with SPEs while reporting directly to CEO; Kopper reported to Fastow and also served as managing director of LJM2; Causey as CAO managed accounting and reported to CEO/COO; Skilling as COO/CEO supervised business units and financial managers but delegated LJM oversight details; hierarchical distance between decision-makers and transaction negotiators created control gaps where Fastow's subordinates negotiated against LJM while reporting to Fastow. | Fastow CFO; Kopper managing director; Causey CAO; Skilling COO/CEO | 1998 to October 2001 | E37, E38, E39 |
| Ford Pinto | ●●● strong (n=12, 4 docs) | Crash test results showing fuel tank vulnerability were forwarded up the chain of command from engineers to vice presidents (Alexander, MacDonald) who chaired product review meetings where decisions to defer corrective action were made, while lower-level engineers aware of defects were powerless to change design decisions. | Lee Iacocca; Robert Alexander; Harold MacDonald; Engineers (Copp, Kennedy, Johnson, Jurosek) | 1968-1971 | E40, E41, E42 |
| Purdue OxyContin | ●●● strong (n=40, 12 docs) | The Sackler family owned and controlled Purdue through board majority, with blurred boundaries between board, management, and shareholders; they directly overruled executives' sales targets, demanded detailed reports on high-volume prescribers and problem doctors, and micromanaged sales operations through direct pressure on executives and sales staff. | Sackler family; Richard Sackler; executives; sales representatives | 2007 to 2018 | E43, E44, E45 |

### Rules of the game and attention-directing incentives

| Case | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Boeing 737MAX | ●●● strong (n=79, 16 docs) | Boeing's financial incentives, production schedules, and performance metrics prioritized cost reduction and schedule adherence over safety considerations, making schedule compliance and cost savings salient while rendering safety risks and comprehensive testing invisible to decision-makers. | Boeing senior program officials; Boeing employees; Boeing management; FAA | 2011-2019 | E46, E47, E48 |
| Dieselgate | ●●● strong (n=40, 10 docs) | Regulatory rules and incentives made laboratory test compliance (NEFZ) the only binding metric for emissions, making real-world emissions invisible; manufacturers could choose lenient approval authorities and technical services based on fees, creating incentives to avoid scrutiny; compliance factors allowed legal exceedances of limits; and manufacturer self-certification with minimal oversight made cheating undetectable. | VW employees; EU regulators; Type approval authorities; Technical services | 2006-2015 | E49, E50, E51 |
| Enron | ●●● strong (n=71, 15 docs) | Enron's formal rules, metrics, and incentives—including stock option awards, earnings targets, performance review systems, and compensation tied to meeting analyst expectations—directed attention to short-term stock price and reported earnings growth, making financial manipulation salient and legitimate business operations invisible. | Skilling; Lay; Fastow; Causey | 1990s through 2001 | E52, E53, E54 |
| Ford Pinto | ●●● strong (n=13, 4 docs) | Ford's product objectives—weight limit of 2,000 pounds, cost limit of $2,000, and compressed 25-month schedule—created salient priorities that made safety invisible; these metrics were enforced by management and excluded safety from formal objectives, causing engineers to deprioritize safety improvements even when crash tests revealed defects. | Lee Iacocca; Pinto engineers; Ford management | 1968 to 1971 | E55, E56, E57 |
| Purdue OxyContin | ●●● strong (n=51, 12 docs) | Purdue's formal compensation system tied sales representatives' bonuses, performance reviews, and employment to prescription volume metrics, making opioid sales the dominant priority and rendering addiction risks and diversion concerns invisible to decision-making. | Purdue sales representatives; Sackler family; Purdue executives | 1996 to 2018 | E58, E59, E60 |

### Focus of attention and dominant agendas

| Case | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Boeing 737MAX | ●●● strong (n=52, 18 docs) | Boeing decision makers prioritized production volume and schedule adherence over design mitigation, while FAA management shifted focus from regulatory compliance to accommodating industry positions and applicant costs. | Boeing senior executives; Boeing program management; FAA management | 2013-2018 | E61, E62, E63 |
| Dieselgate | ●●● strong (n=32, 9 docs) | Decision makers focused on meeting NOx emissions standards and achieving market success in the U.S. diesel market, with attention to test procedures, fuel economy, vehicle performance, and marketing claims of "clean diesel," while regulatory authorities focused on type approval procedures rather than real-world emissions verification. | VW engineers and managers; CARB; EPA; KBA | 2007-2015 | E64, E65, E66 |
| Enron | ●●● strong (n=52, 15 docs) | Decision makers focused intensely on meeting quarterly and annual earnings targets, revenue growth, stock price, credit ratings, and analyst expectations, with these metrics dominating strategy, budget-setting, and transaction decisions even when actual business performance could not support them. | Skilling; Causey; Fastow; Lay | 1997-2001 | E67, E68, E69 |
| Ford Pinto | ●●● strong (n=12, 4 docs) | Ford's decision makers focused on cost savings, production timelines, and market competition (beating Volkswagen and Japanese competitors) rather than fuel system safety, with management unwilling to deviate from design if changes cost money, even when engineers expressed concerns about tank integrity and crash testing revealed vulnerability at low-speed rear impacts. | Ford management; Iacocca; Harley Copp; chief chassis engineer | late 1968 or early 1969; rush project period | E70, E71, E72 |
| Purdue OxyContin | ●●● strong (n=55, 12 docs) | Purdue executives and the Sackler family focused intensely on OxyContin sales revenue, profit growth, and market share, with board meetings and emails repeatedly addressing sales targets, declining prescriptions, high-dose prescribing rates, and financial returns from specific market segments. | Richard Sackler; Sackler family; John Stewart | 2007 to 2018 | E73, E74, E75 |

### Filtering, discounting and neglect of warnings

| Case | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Boeing 737MAX | ●●● strong (n=134, 21 docs) | Boeing employees intentionally withheld and concealed from the FAA critical information about MCAS's expanded operational scope, deleted MCAS references from certification documents, and misled regulators about the system's capabilities, preventing decision makers from understanding the true scope of the hazard. | Boeing employees; FAA Aircraft Evaluation Group; Boeing senior executives | 2016-2017 | E76, E77, E78 |
| Dieselgate | ●●● strong (n=61, 9 docs) | Warnings about emissions discrepancies and defeat devices were systematically dismissed, reframed as legal test optimization, routed to lower-level officials without authority to act, and never reached senior decision-makers who could have stopped the practice. Regulators accepted technical explanations without verification, narrowed investigations to statistical procedures that allowed single cases to be dismissed, and failed to test beyond the NEDC standard despite evidence of real-world emissions problems. | VW engineers and managers; EPA and CARB regulators; German federal authorities; Type-approval technical services | 2007 to September 2015 | E79, E80, E81 |
| Enron | ●●● strong (n=128, 16 docs) | Warnings and concerns about fraudulent transactions were filtered through narrowly scoped investigations, reframed by outside counsel, routed to people without authority to act, and kept from decision makers through incomplete disclosures and selective information flow. | Vinson & Elkins; Enron Board; Arthur Andersen; Fastow | 1999 to October 2001 | E82, E83, E84 |
| Ford Pinto | ●●● strong (n=8, 4 docs) | Ford engineers' safety warnings about fuel tank integrity were filtered out through organizational structures that prioritized styling over safety, failed to route concerns to decision makers (only two people attended a scheduled safety presentation), and management dismissed redesign recommendations based on cost rather than engineering standards. | Ford engineers; Ford management; Lou Tubben; Harold MacDonald | By 1971; meetings timing not stated | E85, E86, E87 |
| Purdue OxyContin | ●●● strong (n=58, 12 docs) | Purdue's ADD Program systematically filtered, delayed, and narrowed warnings about problematic prescribers through high thresholds for reporting, limited field inquiries, reversed decisions on Region Zero placements, and allowed continued marketing despite red flags, while board members claimed unfamiliarity with these practices. | Purdue Pharma; ADD Program; Sackler family board members | 1996 to 2018 | E88, E89, E90 |

### Organizational responses and moves

| Case | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Boeing 737MAX | ●●● strong (n=100, 20 docs) | Boeing delayed fixes, deferred disclosures about MCAS, issued misleading advisories without naming the system, and resisted transparency with regulators while continuing production and sales despite internal safety concerns. | Boeing senior management; Boeing engineers; FAA; Boeing Flight Technical Team | November 2018 to 2019 | E91, E92, E93 |
| Dieselgate | ●●● strong (n=73, 15 docs) | VW systematically concealed the defeat device from regulators through false certifications, misleading technical explanations, selective presentation of test results, and deliberate omission of material facts in applications for emissions compliance, while proposing false remedies and deleting incriminating documents. | Volkswagen AG; EPA; CARB; Winterkorn | 2007 to September 2015 | E94, E95, E96 |
| Enron | ●●● strong (n=71, 15 docs) | Enron management systematically deferred, concealed, and manipulated financial disclosures and accounting treatments in response to signals of business problems and losses, including restructuring transactions, back-dating documents, delaying disclosures, and manufacturing false transactions to avoid reporting losses and maintain financial targets. | Causey; Fastow; Skilling; Lay | 2000-2001 | E97, E98, E99 |
| Ford Pinto | ●●● strong (n=46, 6 docs) | Ford deferred safety improvements to the Pinto's fuel tank through cost-benefit analysis, lobbied against government safety standards for years, and used multiple rhetorical techniques to delay regulations. | Ford Motor Company; NHTSA; Ford engineers; Ford lobbyists | 1968 to 1978 | E100, E101, E102 |
| Purdue OxyContin | ●●● strong (n=65, 12 docs) | Purdue received signals of abuse and diversion but responded by continuing to target high-volume prescribers, resuming calls on flagged prescribers, intensifying marketing through E2E, and deferring fixes while concealing evidence. | Purdue Pharma; Sackler family; Sales representatives | 2000-2018 | E103, E104, E105 |

### Attention shifts and triggering events

| Case | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Boeing 737MAX | ●●● strong (n=60, 18 docs) | Two fatal crashes (Lion Air October 2018, Ethiopian Airlines March 2019) triggered immediate regulatory grounding, congressional investigations, media scrutiny, and internal Boeing safety reviews that redirected organizational attention to MCAS design and certification processes. | FAA; Boeing; Congress; NTSB | October 2018 to March 2019 | E106, E107, E108 |
| Dieselgate | ●●● strong (n=34, 10 docs) | External triggering events—the ICCT study results, EPA Notice of Violation, and public disclosure—redirected organizational attention and prompted observable changes in VW's priorities, agendas, and leadership structure, including executive briefings, management requests for situation updates, leadership resignations, and restructuring of business units. | EPA; CARB; VW senior management; Winterkorn | March 2014 to September 2015 | E109, E110, E111 |
| Enron | ●●● strong (n=46, 14 docs) | Media exposés (Wall Street Journal articles on October 17, 2001) and subsequent regulatory inquiries (SEC investigation) redirected organizational attention from normal operations to crisis management, prompting board investigations, leadership changes, and strategic responses including Fastow's removal. | Wall Street Journal; SEC; Enron Board; Andrew Fastow | August 2001 to December 2001 | E112, E113, E114 |
| Ford Pinto | ●●● strong (n=12, 5 docs) | Lawsuits from rear-end Pinto collisions and media exposés triggered NHTSA to launch crash testing investigations, which led to formal safety defect determinations and a recall of 1.5 million vehicles. | NHTSA; Ford Motor Co.; lawyers; recon men | 1977-1978 | E115, E116, E117 |
| Purdue OxyContin | ●●● strong (n=34, 12 docs) | Multiple triggering events—congressional hearings and law enforcement focus (2001), DOJ investigation and 2007 felony settlement, FDA label changes, state lawsuits (post-2007), and media exposés (2019)—redirected organizational attention and prompted observable responses including leadership resignations, consulting engagement for sales targeting, document destruction protocols, and bankruptcy filing. ⚠ | Purdue Pharma; Sackler family; Department of Justice; State attorneys general | 1999 to 2019 | E118, E119, E120 |

## Evidence

**E1.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 197

> In June 2016, more than two years prior to the October 2018 crash of the Lion Air flight, Boeing engineers had predicted some of the key issues that led to the Lion Air crash, including the potential adverse consequences of erroneous AOA sensor data on MCAS, and they questioned whether or not pilots would have trouble combatting repetitive MCAS activation. These concerns, however, were either not adequately addressed or largely dismissed by their Boeing colleagues.

**E2.** Boeing 737MAX, *SEC_Order_Muilenburg_33-11106_2022-09-22*, p. 6

> On or about November 15, 2016, during a test flight of the 737 MAX in a simulator, Boeing Employee-1 experienced what Boeing Employee-1 recognized as MCAS operating at lower speed. Later that day, Boeing Employee-1 and Boeing Employee-2 discussed MCAS in an electronic chat (the "November 15, 2016 Chat") which contained the following exchange: Boeing Employee-1: Oh shocker alerT! / MCAS is now active down to M[ach] .2 / It's running rampant in the sim[ulator] on me… / so I basically lied to the r…

**E3.** Boeing 737MAX, *SEC_Order_Boeing_33-11105_2022-09-22*, p. 7

> On November 7, 2018, the FAA issued a public emergency airworthiness directive to airlines operating the 737 MAX, informing them of the potential for repeated nose-down movements of the aircraft which, "if not addressed, could cause the flight crew to have difficulty controlling the airplane … and [could result in] possible impact with terrain." The airworthiness directive identified the issue as an "unsafe condition" on the 737 MAX, and, as an "interim action" pending further analysis, referred…

**E4.** Dieselgate, *ICCT_WVU_InUse_Emissions_Testing_Report_2014*, p. 2

> Real-world NOx emissions were found to exceed the US-EPA Tier2-Bin5 (at full useful life) standard by a factor of 15 to 35 for the LNT-equipped vehicle, by a factor of 5 to 20 for one and at or below the standard for the second urea-SCR fitted vehicle over five pre-defined routes categorized based on their predominant driving conditions, namely, i) highway, ii) urban/suburban, and iii) rural-up/downhill driving.

**E5.** Dieselgate, *House_EC_Majority_Staff_Hearing_Memo_2015-10-06*, p. 4 ≈

> May 2014: A study conducted by independent researchers at West Virginia University (WVU) on behalf of the International Council for Clean Transportation (ICCT) identified significantly higher on-road NOx emissions from two VW vehicles — a 2012 Jetta and a 2013 Passat. The results of this study were brought to the attention of the EPA, CARB, and VW.

**E6.** Dieselgate, *Winterkorn_et_al_Fifth_Superseding_Indictment*, p. 21 ≈

> In or around March 2014, certain VW employees, including NEUSSER, GOTTWEIS, PETER, and WINTERKORN learned of the results of a study undertaken by West Virginia University's Center for Alternative Fuels, Engines and Emissions and commissioned by the International Council on Clean Transportation (the "ICCT study"). The ICCT study identified substantial discrepancies in the NOx emissions from certain 2.0 Liter Subject Vehicles when tested on the road compared to when these vehicles were undergoing …

**E7.** Enron, *Healy_Palepu_2003_The_Fall_of_Enron_JEP*, p. 2

> Sherron Watkins, an Enron vice president, wrote an anonymous letter to Kenneth Lay expressing concerns about the firm's accounting. She subsequently discussed her concerns with James Hecker, a former colleague and audit partner at Andersen, who contacted the Enron audit team.

**E8.** Enron, *Powers_Report_Special_Investigative_Committee_2002-02-01*, p. 172 ≈

> Shortly after Enron announced Skilling's unexpected resignation on August 14, 2001, Watkins sent a one-page anonymous letter to Lay. The letter stated that "Enron has been very aggressive in its accounting--most notably the Raptor transactions." The letter raised serious questions concerning the accounting treatment and economic substance of the Raptor transactions (and transactions between Enron and Condor Trust, a subsidiary of Whitewing Associates), identifying several of the matters discusse…

**E9.** Enron, *Senate_PSI_Role_of_Board_in_Enrons_Collapse_2002*, p. 22 ≈

> An email dated February 6, 2001, sent to David Duncan and Thomas Bauer by another Andersen partner, Michael D. Jones, offers further proof that Andersen viewed Enron as engaged in risky accounting. This email summarizes a meeting held the previous day by 14 senior Andersen partners to decide whether the firm should retain Enron as a client. The email indicates that the group was aware of and uneasy about a number of accounting practices and transactions at Enron. The email, included in Hearing E…

**E10.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> Ford engineers discovered in pre-production crash tests that rear-end collisions would rupture the Pinto's fuel system extremely easily.

**E11.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> Internal company documents in our possession show that Ford has crash-tested the Pinto at a top-secret site more than 40 times and that every test made at over 25 mph without special structural alteration of the car has resulted in a ruptured fuel tank.

**E12.** Ford Pinto, *Grimshaw_v_Ford_Motor_Co_1981_CalCtApp_119CalApp3d757*, p. 775

> The crash tests revealed that the Pinto's fuel system as designed could not meet the 20-mile-per-hour proposed standard. Mechanical prototypes struck from the rear with a moving barrier at 21 miles per hour caused the fuel tank to be driven forward and to be punctured, causing fuel leakage in excess of the standard prescribed by the proposed regulation. A production Pinto crash tested at 21 miles per hour into a fixed barrier caused the fuel neck to be torn from the gas tank and the tank to be p…

**E13.** Purdue OxyContin, *House_Oversight_Supplemental_Staff_Memo_2020-12-14*, p. 3 ≈

> Documents obtained by DOJ also show that Purdue executives and members of the Sackler family ignored safeguards from the company's Abuse and Diversion Detection program—intended to identify and cut off heath care providers suspected of suspicious prescribing behavior. Although members of the Sackler family were routinely informed of red flags raised by the program, many high-volume prescribers went unreported. Even in cases when they were reported, Purdue continued to deploy sales representative…

**E14.** Purdue OxyContin, *Massachusetts_AG_First_Amended_Complaint_Purdue_Sacklers_2019-01-31*, p. 65

> In July 2007, staff told the Sacklers that more than 5,000 cases of adverse events had been reported to Purdue in just the first three months of 2007. Staff also told the Sacklers that Purdue received 572 Reports of Concern about abuse and diversion of Purdue opioids during Q2 2007 — including several reports in Massachusetts. Staff reported to the Sacklers that they completed only 21 field inquiries in response. Staff also told the Sacklers that they received more than 100 calls to Purdue's com…

**E15.** Purdue OxyContin, *Massachusetts_AG_First_Amended_Complaint_Purdue_Sacklers_2019-01-31*, p. 232

> Seventeen patients who were prescribed Purdue opioids by Mashali died of opioid overdoses. Purdue's sales reps visited Mashali and Jayma more than 195 times, and Purdue management ordered the reps to keep promoting opioids to them, even after reps warned Purdue that they were dangerous prescribers.

**E16.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 100

> The FAA was not completely unaware of MCAS; however, because the information and discussions about MCAS were so fragmented and were delivered to disconnected groups within the process, it was difficult to recognize the impacts and implications of this system. If the FAA technical staff had been fully aware of the details of MCAS function, the JATR team believes the agency likely would have required an issue paper for using the stabilizer in a way that it had not previously been used.

**E17.** Boeing 737MAX, *Boeing_DPA_incl_Statement_of_Facts_2021-01-07*, p. 35

> Boeing disclosed this expansion to FAA personnel, but only to those personnel who were responsible for determining whether the 737 MAX met U.S. federal airworthiness standards. Boeing did not disclose the expansion to the FAA AEG personnel responsible for publishing the 737 MAX FSB Report and making the training-related determination.

**E18.** Boeing 737MAX, *JATR_Joint_Authorities_Technical_Review_2019-10*, p. 44

> Although MCAS may have been briefed to some FAA personnel, key aspects of the MCAS function such as intended function description, its interfaces, and architecture, were not directly visible to the FAA in a straightforward manner through the certification deliverable documents.

**E19.** Dieselgate, *DOJ_EPA_Amended_Civil_Complaint_2016*, p. 21 ≈

> Between 2006 and 2014, employees in Volkswagen AG's Powertrain Development division, including managers, regularly communicated with each other, and contractors, regarding the design and later refinements of the dual-mode strategy, referred to as the "extended Akustikfunktion," among other aliases.

**E20.** Dieselgate, *Winterkorn_et_al_Fifth_Superseding_Indictment*, p. 23

> Following the ICCT study, CARB, in coordination with the EPA, attempted to work with VW to determine the cause for the higher NOx emissions in 2.0 Liter Subject Vehicles when being driven on the road as opposed to on the dynamometer undergoing standard emissions test cycles. To do this, CARB, in coordination with the EPA, repeatedly asked VW questions that became increasingly more specific and detailed, as well as conducted additional testing themselves.

**E21.** Dieselgate, *VW_Third_Superseding_Information_2017*, p. 2 ≈

> To obtain a certificate of conformity, a manufacturer was required to submit an application to the EPA for each model year and for each test group of vehicles that it intended to sell in the United States. The application was required to be in writing, to be signed by an authorized representative of the manufacturer, and to include, among other things, the results of testing done pursuant to the published Federal Test Procedures that measure NOx emissions, and a description of the engine, emissi…

**E22.** Enron, *Powers_Report_Special_Investigative_Committee_2002-02-01*, p. 10

> Over time, the Board required, and Management told the Board it was implementing, an ever-increasing set of procedures and controls over the related-party transactions. These included, most importantly, review and approval of all LJM transactions by Richard Causey, the Chief Accounting Officer; and Richard Buy, the Chief Risk Officer; and, later during the period, Jeffrey Skilling, the President and COO (and later CEO). The Board also directed its Audit and Compliance Committee to conduct annual…

**E23.** Enron, *Fastow_Complaint_Affidavit_2002*, p. 14 ≈

> According to interviews of Board members, and review of Board minutes and Board members' contemporaneous notes, in approving FASTOW's role at LJM the Board relied on false representations by FASTOW, Enron's Chief Executive Officer (CEO), Chief Accounting Officer (CAO), Treasurer, and others. Specifically, the Board understood that: (1) Enron's CAO and Chief Risk Officer would review transactions with LJM to ensure their fairness to Enron; (2) the Board would be informed of all Enron transactions…

**E24.** Enron, *Powers_Report_Special_Investigative_Committee_2002-02-01*, p. 23 ≈

> The Audit and Compliance Committee, and later the Finance Committee, took on a specific role in the control structure by carrying out periodic reviews of the LJM transactions. This was an opportunity to probe the transactions thoroughly, and to seek outside advice as to any issues outside the Board members' expertise. Instead, these reviews appear to have been too brief, too limited in scope, and too superficial to serve their intended function.

**E25.** Ford Pinto, *Grimshaw_v_Ford_Motor_Co_1981_CalCtApp_119CalApp3d757*, p. 776

> During the course of the project, regular product review meetings were held which were chaired by Mr. MacDonald and attended by Mr. Alexander. As the project approached actual production, the engineers responsible for the components of the project "signed off" to their immediate supervisors who in turn "signed off" to their superiors and so on up the chain of command until the entire project was approved for public release by Vice Presidents Alexander and MacDonald and ultimately by Mr. Iacocca.

**E26.** Ford Pinto, *Grimshaw_v_Ford_Motor_Co_1981_CalCtApp_119CalApp3d757*, p. 776

> As the project approached actual production, the engineers responsible for the components of the project "signed off" to their immediate supervisors who in turn "signed off" to their superiors and so on up the chain of command until the entire project was approved for public release by Vice Presidents Alexander and MacDonald and ultimately by Mr. Iacocca. The Pinto crash tests results had been forwarded up the chain of command to the ultimate decision-makers and were known to the Ford officials …

**E27.** Ford Pinto, *Grimshaw_v_Ford_Motor_Co_1981_CalCtApp_119CalApp3d757*, p. 776

> The Pinto crash tests results had been forwarded up the chain of command to the ultimate decision-makers and were known to the Ford officials who decided to go forward with production.

**E28.** Purdue OxyContin, *Massachusetts_AG_First_Amended_Complaint_Purdue_Sacklers_2019-01-31*, p. 179

> In February, Purdue's Sales and Marketing Department reported to Boer, Lewent, and Pickett that a key objective for 2010 was meeting a prescriber sales call quota of 545,000. Sales call quotas remained a priority over the next four years, and the Board tracked the sales force's performance on at least a quarterly basis as the quota rose from 545,000 prescriber visits in 2010, to 712,000 visits in 2011, 752,417 visits in 2012, and 744,777 visits in 2013.

**E29.** Purdue OxyContin, *DOJ_Purdue_Civil_Settlement_Agreement_2020-10*, p. 48 ≈

> At all relevant times, Purdue maintained an ADD program, through which Purdue had the means and ability to identify prescribers suspected of engaging in abuse and diversion. The ADD program began in or around 2002 and ended in or around February 2018. It was governed during most of that time period by Standard Operating Procedure ("SOP") 1.7.1. SOP 1.7.1 instructed Purdue employees to refer prescribers who displayed indicia of abuse and diversion to ADD. Employees referred these prescribers to A…

**E30.** Purdue OxyContin, *Purdue_Plea_Agreement_2020-10-20*, p. 72 ≈

> Purdue sales representatives were trained to report prescribers suspected of abuse and diversion to ADD, and some sales representatives did so. However, high-volume prescribers were often not reported and, even if they were, they were sometimes not added to Region Zero until they lost the ability to prescribe through legal or medical board action. In addition, certain Purdue policies resulted in high-volume prescribers not being reported to ADD, and thus not being added to Region Zero. For examp…

**E31.** Boeing 737MAX, *Boeing_DPA_incl_Statement_of_Facts_2021-01-07*, p. 35

> Subsequently, Boeing expanded MCAS's operational scope, including the speed range within which MCAS could activate, significantly altering its original design. Among other things, when the airplane registered a high angle of attack, the change expanded the speed range within which MCAS could activate from approximately Mach 0.6-0.8 to approximately Mach 0.2-0.8—that is, from only high-speed flight to nearly the entire speed range for the 737 MAX, including low-speed flight, which generally occur…

**E32.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 51

> Boeing Employee-1 and Boeing Employee-2 understood that the FAA AEG relied on them, as members of Boeing's 737 MAX Flight Technical Team, to identify and provide to the FAA AEG all information that was relevant to the FAA AEG in connection with the FAA AEG's publication of the 737 MAX FSB Report, including information that could impact the FAA AEG's differences-training determination.

**E33.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 27

> In March 2016, the General Manager of Boeing's 737 MAX program, Keith Leverkuhn, and Michael Teal, the former Chief Project Engineer on the 737 MAX program, both approved a redesign of MCAS to increase its authority to move the aircraft's stabilizer at low speed, in order to address "stall characteristics" requirements necessary for FAA certification.

**E34.** Dieselgate, *Winterkorn_et_al_Fifth_Superseding_Indictment*, p. 10

> From on or about January 1, 2007 until on or about September 23, 2015, MARTIN WINTERKORN was the Chief Executive Officer and Chairman of the Management Board ofVW AG. All employees ofVW reported to WINTERKORN. From in or about July 2013 until in or about September 2015, NEUSSER reported directly to WINTERKORN.

**E35.** Dieselgate, *Dorenkamp_et_al_Second_Superseding_Indictment*, p. 9 ≈

> From in or about July 2013 until in or about September 2015, defendant HEINZ-JAKOB NEUSSER worked for VW AG as the head of Development for VW Brand, sat on the management board for VW Brand, and also served as head of Engine Development for all of VW AG. From in or about October 2011, when he joined VW from Porsche, until in or about July 2013, NEUSSER served as the head of the VW Brand Engine Development department. In his capacity as head of Development for VW Brand, NEUSSER supervised a group…

**E36.** Dieselgate, *Dorenkamp_et_al_Second_Superseding_Indictment*, p. 9 ≈

> From in or about May 2007 until in or about March 2011, defendant JENS HADLER worked for VW AG as the head of the VW Brand Engine Development department. Before serving as head of Engine Development, HADLER held various positions within VW AG, including as head of Diesel Engine Development for VW from in or about 2003 until in or about October 2006. As a result of the meeting, HADLER authorized DORENKAMP to proceed with the US '07 project despite knowing that only the use of the defeat device so…

**E37.** Enron, *Powers_Report_Special_Investigative_Committee_2002-02-01*, p. 18

> Fastow was Enron's Chief Financial Officer and was involved on both sides of the related-party transactions. What he presented as an arrangement intended to benefit Enron became, over time, a means of both enriching himself personally and facilitating manipulation of Enron's financial statements. Both of these objectives were inconsistent with Fastow's fiduciary duties to Enron and anything the Board authorized.

**E38.** Enron, *Powers_Report_Special_Investigative_Committee_2002-02-01*, p. 166

> In many cases, the safeguard requiring that a transaction could be negotiated on behalf of Enron only by employees who did not report to Fastow was ignored. We have identified at least 13 transactions between Enron and LJM2 in which the individuals negotiating on behalf of Enron reported directly or indirectly to Fastow.

**E39.** Enron, *SEC_Complaint_Skilling_Causey_2004* ≈

> In December 1996, Enron promoted Skilling to President and COO of the entire company, reporting directly to Enron's Chief Executive Officer ("CEO") and Chairman. In February 2001, Skilling became CEO of Enron and retained his position as COO. As COO and CEO of Enron, Skilling was the senior manager of the company's commercial operations and finances and one of its principal spokespersons with the investing public. Skilling closely supervised on a day-to-day basis the activities of each of Enron'…

**E40.** Ford Pinto, *Grimshaw_v_Ford_Motor_Co_1981_CalCtApp_119CalApp3d757*, p. 813

> There is substantial evidence that management was aware of the crash tests showing the vulnerability of the Pinto's fuel tank to rupture at low speed rear impacts with consequent significant risk of injury or death of the occupants by fire. There was testimony from several sources that the test results were forwarded up the chain of command; vice president Robert Alexander admitted to Mr. Copp that he was aware of the test results; vice president Harold MacDonald, who chaired the product review …

**E41.** Ford Pinto, *Grimshaw_v_Ford_Motor_Co_1981_CalCtApp_119CalApp3d757*, p. 777

> The fact that two of the crash tests were run at the request of the Ford chassis and vehicle engineering department for the specific purpose of demonstrating the advisability of moving the fuel tank over the axle as a possible "fix" further corroborated Mr. Copp's testimony that management knew the results of the crash tests. Mr. Kennedy, who succeeded Mr. Copp as the engineer in charge of Ford's crash testing program, admitted that the test results had been forwarded up the chain of command to …

**E42.** Ford Pinto, *Grimshaw_v_Ford_Motor_Co_1981_CalCtApp_119CalApp3d757*, p. 776 ≈

> In 1968, Ford began designing a new subcompact automobile which ultimately became the Pinto. Mr. Iacocca, then a Ford vice president, conceived the project and was its moving force. The feasibility study was conducted under the supervision of Mr. Robert Alexander, vice president of car engineering. Ford's Product Planning Committee, whose members included Mr. Iacocca, Mr. Robert Alexander, and Mr. Harold MacDonald, Ford's group vice president of car engineering, approved the Pinto's concept and …

**E43.** Purdue OxyContin, *Massachusetts_AG_First_Amended_Complaint_Purdue_Sacklers_2019-01-31*, p. 54

> The Sackler family owns Purdue, and they always held a majority of the seats on its Board. Because they controlled their own privately held drug company, the Sacklers had the power to decide how addictive narcotics were sold. They hired hundreds of workers to carry out their wishes, and they fired those who didn't sell enough drugs.

**E44.** Purdue OxyContin, *DOJ_Purdue_Civil_Settlement_Agreement_2020-10*, p. 34

> By virtue of OxyContin's importance, certain of the Sacklers placed pressure on executives to meet OxyContin sales goals set by the Board and participated in decision-making regarding Purdue's sales strategies for OxyContin, at times overruling the targets set by Purdue's executives.

**E45.** Purdue OxyContin, *Massachusetts_AG_First_Amended_Complaint_Purdue_Sacklers_2019-01-31*, p. 63 ≈

> From 2007 to 2018, the Sackler controlled Purdue's deceptive sales campaign. They directed the company to hire hundreds more sales reps to visit doctors thousands more times. They insisted that sales reps repeatedly visit the most prolific prescribers. They directed reps to encourage doctors to prescribe more of the highest doses of opioids. They studied unlawful tactics to keep patients on opioids longer and then ordered staff to use them. They asked for detailed reports about doctors suspected…

**E46.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 24

> In 2012, in order to lower costs of the 737 MAX program, Boeing reduced the work hours involved in avionics regression testing on the 737 MAX by 2,000 hours. It also examined other reductions to save costs, including a reduction to flight test support by 3,000 hours and a reduction to the engineering flight deck simulator (E-CAB) by 8,000 hours.

**E47.** Boeing 737MAX, *House_TI_Hearing_FAA_Oversight_Pierson_testimony_2019-12-11*, p. 133

> For example, it was reported in the media that a survey found that one in three Boeing employees reported they felt undue pressure from managers regarding safety-related approvals due to time and schedule concerns, and some 15% reported encountering such problems several times or frequently.

**E48.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 24 ≈

> To emphasize the significance of the 737 MAX program's schedule to Boeing employees, the Committee learned that senior program officials kept a "countdown clock" in their conference room. Keith Leverkuhn, the former Vice President and General Manager of the MAX program, described the clock as an "excitement generator" for Boeing's staff. But he also acknowledged it was to remind staff about the MAX's schedule. "One of the mantras that we had was the value of a day," he said, "and making sure tha…

**E49.** Dieselgate, *EuroParl_EMIS_Inquiry_Final_Report_A8-0049-2017*, p. 54 ≈

> In their written answers and during the hearings, Member States and car manufacturers stated that they interpreted the legislation in such a way that the NEDC test in the laboratory was the only requirement for vehicles to pass, despite the air-quality objectives of the legislation.

**E50.** Dieselgate, *Bundestag_Abgas_Untersuchungsausschuss_Report_Drs18-12900_2017_DE*, p. 389 ≈

> Lassen Sie mich die Frage so beantworten: Nein; denn der NEFZ ist der einzig verbindliche Maßstab, sozusagen die Messlatte dessen, was gelten darf und gelten kann. Andererseits: Ja, hätten wir Anlass im Sinne von Indizien gehabt – und seien es auch nur Anfangsindizien – dass vielleicht, womöglich etwas nicht ganz vorschriftenkonform gelaufen sein könnte, hätten wir in jedem Fall auch rechtlich die Möglichkeit gehabt, ergänzende Prüfungen vorzunehmen. Aber verbindlich ist, dass der NEFZ – noch ma…

**E51.** Dieselgate, *EuroParl_EMIS_Inquiry_Final_Report_A8-0049-2017*, p. 11

> Car manufacturers are, in principle, free to address the type-approval authority and technical service with the most flexible and least stringent interpretation of the rules, as well as the lowest fees.

**E52.** Enron, *Healy_Palepu_2003_The_Fall_of_Enron_JEP*, p. 11

> Heavy use of stock option awards linked to short-term stock price may explain the focus of Enron's management on creating expectations of rapid growth and its efforts to puff up reported earnings to meet Wall Street's expectations. In its 2001 proxy statement, Enron noted that within 60 days of the proxy date (February 15), the following stock option awards would become exercisable: 5,285,542 shares for Kenneth Lay, 824,038 shares for Jeff Skilling and 12,611,385 shares for all officers and dire…

**E53.** Enron, *SEC_Complaint_Skilling_Causey_2004*

> Skilling and Causey set annual and quarterly earnings and cash flow targets ("budget targets") for the company and each of its business units. They did so by determining the numbers necessary to meet analysts' expectations, rather than what could be realistically achieved by legitimate business operations.

**E54.** Enron, *Causey_Indictment_2004*, p. 4

> The scheme's objectives were, among other things, to produce reported earnings that steadily grew by approximately 15 to 20 percent every year; to meet or exceed, without fail, the published expectations of industry analysts forecasting Enron's reported earnings-per-share results; to avoid publicly reporting any large "write-downs" or losses; to persuade investors that Enron's future profitability would continue to grow; and to deceive lenders, rating agencies, and the investing public about the…

**E55.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> Heightening the anti-safety pressure on Pinto engineers was an important goal set by Iacocca known as "the limits of 2,000." The Pinto was not to weigh an ounce over 2,000 pounds and not to cost a cent over $2,000. "Iacocca enforced these limits with an iron hand," recalls the engineer quoted earlier. So, even when a crash test showed that that one-pound, one-dollar piece of plastic stopped the puncture of the gas tank, it was thrown out as extra cost and extra weight.

**E56.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo* ≈

> The product objectives are clearly stated in the Pinto "green book." This is a thick, top-secret manual in green covers containing a step-by-step production plan for the model, detailing the metallurgy, weight, strength and quality of every part in the car. The product objectives for the Pinto are repeated in an article by Ford executive F.G. Olsen published by the Society of Automotive Engineers. He lists these product objectives as follows: 1. TRUE SUBCOMPACT... 2. LOW COST OF OWNERSHIP... 3. …

**E57.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> "Hell no," replied an engineer who worked on the Pinto, a high company official for many years, who, unlike several others at Ford, maintains a necessarily clandestine concern for safety. "That person would have been fired. Safety wasn't a popular subject around Ford in those days. With Lee it was taboo. Whenever a problem was raised that meant a delay on the Pinto, Lee would chomp on his cigar, look out the window and say 'Read the product objectives and get back to work.'"

**E58.** Purdue OxyContin, *Massachusetts_AG_First_Amended_Complaint_Purdue_Sacklers_2019-01-31*, p. 12

> Purdue judged its sales reps by how many opioids they got doctors to prescribe. Sales reps who generated the most prescriptions won bonuses and prizes. Reps who failed to get enough Massachusetts patients on opioids were placed on probation, put on performance improvement plans, and fired.

**E59.** Purdue OxyContin, *VanZee_2009_Promotion_and_Marketing_of_OxyContin_AJPH*, p. 2

> A lucrative bonus system encouraged sales representatives to increase sales of OxyContin in their territories, resulting in a large number of visits to physicians with high rates of opioid prescriptions, as well as a multifaceted information campaign aimed at them. In 2001, in addition to the average sales representative's annual salary of $55 000, annual bonuses averaged $71500, with a range of $15 000 to nearly $240 000. Purdue paid $40 million in sales incentive bonuses to its sales represent…

**E60.** Purdue OxyContin, *Massachusetts_AG_First_Amended_Complaint_Purdue_Sacklers_2019-01-31*, p. 158

> That same month, the Sacklers voted to evaluate employees' 2014 performance on a scorecard that assigned the greatest value to the volume of Purdue opioid sales. Employees were expected to generate more than one-and-a-half billion dollars. The Sacklers also voted to establish the company's scorecard for 2015: once again, the biggest factor determining employees' payout would be the total amount of Purdue opioid sales.

**E61.** Boeing 737MAX, *Boeing_Non-Prosecution_Agreement_2025-05-29*, p. 18

> Boeing senior executives prioritized the movement of aircraft through Boeing's factories over reducing out-of-sequence work to ensure production quality.

**E62.** Boeing 737MAX, *SEC_Order_Muilenburg_33-11106_2022-09-22*, p. 8

> On November 20, 2018, Muilenburg expressed disappointment in Boeing's response to the negative post-crash media coverage, stating in an email that "[w]e are spending too much time playing defense… [we] need to start playing some offense."

**E63.** Boeing 737MAX, *House_TI_Hearing_FAA_Oversight_Pierson_testimony_2019-12-11*, p. 261

> FAA management has changed their focus from one that prioritized compliance to regulations and policy thirty years ago to a management culture that gives priority to applicants' positions, their costs and schedules over compliance to FAA regulations and policy.

**E64.** Dieselgate, *Winterkorn_et_al_Fifth_Superseding_Indictment*, p. 14

> DOREN.KAMP, HADLER, and their co-conspirators, however, realized that they could not design a diesel engine that would both meet the stricter NOx emissions standards that would become effective in 2007 and attract sufficient customer demand in the U.S. market. Instead of bringing to market a diesel vehicle that could legitimately meet the heightened U.S. NOx emissions standards, VW employees acting at the direction of DOREN.KAMP, HADLER, and their co-conspirators, designed, created, and implemen…

**E65.** Dieselgate, *Winterkorn_et_al_Fifth_Superseding_Indictment*, p. 17

> Specifically, Audi engineers calibrated a defeat device for the 3.0 Liter Subject Vehicles that varied injection levels of a solution consisting of urea and water ("AdBlue") into the exhaust gas system based on whether the vehicle was being tested or not, with substantially less NOx reduction occurring during regular driving conditions. In this way, the vehicle consumed less AdBlue, and avoided a corresponding increase in the vehicle's AdBlue tank size, which would have decreased the vehicle's t…

**E66.** Dieselgate, *Winterkorn_et_al_Fifth_Superseding_Indictment*, p. 29

> Starting on or about July 1, 2008, defendants marketed and sold, and caused to be marketed and sold, in the U.S. the Subject Vehicles containing the new "clean diesel" engine, which, in fact, contained the defeat device. A marketing vehicle was painted with green vines and the words "Jetta TDI Clean Diesel" and "goodcleandieselfun.com."

**E67.** Enron, *Skilling_Lay_Causey_Superseding_Indictment*, p. 7 ≈

> Defendants JEFFREY K. SKILLING and RICHARD A. CAUSEY and their coconspirators set the targets by determining the numbers necessary for each Enron business unit to produce in order to meet Enron's mandates for growth and analysts' expectations, rather than by determining how much earnings and cash flow that a particular business unit could reasonably be expected to generate. On a quarterly and year-end basis, SKILLING and CAUSEY and others assessed Enron's progress toward its budget targets. When…

**E68.** Enron, *SEC_Complaint_Skilling_Causey_2004* ≈

> The objectives of the scheme to defraud carried out by Skilling, Causey, and others were, among other things, to produce reported recurring earnings that grew smoothly by approximately 15 to 20 percent annually; to meet or exceed the published expectations of industry analysts forecasting Enron's reported earnings-per-share and other results; to avoid publicly reporting any large "write-downs" or losses; to persuade investors that Enron's profitability would continue to grow; to maintain an inve…

**E69.** Enron, *Causey_Indictment_2004*, p. 2

> The price of Enron's stock was influenced by factors such as Enron's reported revenue, earnings, debt, cash flow (sometimes categorized as "funds flow"), and credit rating, as well as its ability to meet revenue and earnings targets and forecasts. Enron's management, like that of many public companies, provided guidance to the investing public regarding anticipated revenue and earnings for upcoming reporting periods. Relying in part on the company's guidance, many professional securities analyst…

**E70.** Ford Pinto, *Grimshaw_v_Ford_Motor_Co_1981_CalCtApp_119CalApp3d757*, p. 776

> Harley Copp, a former Ford engineer and executive in charge of the crash testing program, testified that the highest level of Ford's management made the decision to go forward with the production of the Pinto, knowing that the gas tank was vulnerable to puncture and rupture at low rear impact speeds creating a significant risk of death or injury from fire and knowing that "fixes" were feasible at nominal cost. He testified that management's decision was based on the cost savings which would inur…

**E71.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> Until recently, it was clear that, whatever the cost of these settlements, it was not enough to seriously cut into the Pinto's enormous profits. The cost of retooling Pinto assembly lines and of equipping each car with a safety gadget like that $5.08 Goodyear bladder was, company accountants calculated, greater than that of paying out millions to survivors like Robbie Carlton or to widows and widowers of victims like Sandra Gillespie. The bottom line ruled, and inflammable Pintos kept rolling ou…

**E72.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo* ≈

> Fighting strong competition from Volkswagen for the lucrative small-car market, the Ford Motor Company rushed the Pinto into production in much less than the usual time. Iacocca argued forcefully that Volkswagen and the Japanese were going to capture the entire American subcompact market unless Ford put out its own alternative to the VW Beetle.

**E73.** Purdue OxyContin, *Massachusetts_AG_First_Amended_Complaint_Purdue_Sacklers_2019-01-31*, p. 64

> The Sacklers cared most of all about money. From 2007 to 2018, they voted to direct Purdue to pay their family billions of dollars, including tens of millions of dollars from opioids sold in Massachusetts. These payments show the total control that the Sacklers exercised over Purdue. The payments were the motivation for the Sacklers' misconduct. And the payments were deliberate decisions to benefit from deception in Massachusetts, at great cost to patients and families.

**E74.** Purdue OxyContin, *House_Oversight_Supplemental_Staff_Memo_2020-12-14*, p. 5

> In March 2008, Dr. Richard Sackler—who is the son of one of Purdue's original owners and has held top positions at the company including President, Chief Executive Officer (CEO), and Chairman of the Board of Directors—sent an email to then-CEO John Stewart criticizing the company's 2008 performance projections. Dr. Sackler wrote: "I really don't like the forecast at this point. I think it is a typical low ball number that people expect to beat and be complimented for. I want the organization to …

**E75.** Purdue OxyContin, *House_Oversight_Supplemental_Staff_Memo_2020-12-14*, p. 5

> In August 2009, Dr. Sackler emailed other members of the Board of Directors concerning declining sales projections for OxyContin. He noted that "the value to us of reversing the current declines of 5-8% and converting them to a 5% growth is worth $1/4 B ($243M) in going from -6.5% to +5.0%; before the decline began, we were growing closer to 10%/yr in the oxycodone ER market. Of no small matter is the profit associated with the incremental sales which at 80% would be ~200M!"

**E76.** Boeing 737MAX, *Boeing_DPA_incl_Statement_of_Facts_2021-01-07*, p. 38

> Despite knowing that the FAA AEG had issued its provisional "Level B" determination without any awareness that MCAS's operational scope had been expanded to include high angle of attack conditions in nearly the entire speed range of ordinary commercial flight, Boeing Employee-1 and Boeing Employee-2 did not correct the FAA AEG's understanding of MCAS's operational scope or otherwise ensure that the FAA AEG's "Level B" determination was based on an accurate understanding of MCAS's operation. Inst…

**E77.** Boeing 737MAX, *Boeing_Criminal_Information_2021-01-07*, p. 2

> On or about January 17, 2017, an employee of THE BOEING COMPANY emailed an employee of the FAA AEG about the 737 MAX FSB Report, stating in part, "Flight Controls: Delete MCAS, recall we decided we weren't going to cover it [. . .] since it's way outside the normal operating envelope."

**E78.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 56 ≈

> At this point, Boeing Employee-1 and Boeing Employee-2 recognized that the FAA AEG was under the misimpression that MCAS operated only during a high-speed, wind up turn and could not operate at lower Mach speeds, such as at Mach 0.2. Boeing Employee-1 and Boeing Employee-2 therefore knew, at least as of the time of this chat communication, that the FAA AEG's provisional 'Level B' differences-training determination had been based in part on outdated and inaccurate information about MCAS. . . . De…

**E79.** Dieselgate, *EuroParl_EMIS_Inquiry_Final_Report_A8-0049-2017*, p. 5

> Before September 2015 the discrepancies were generally attributed to the inadequacy of the NEDC laboratory test, which is not representative of real-world emissions, and to the optimisation strategies put in place by car manufacturers to pass the laboratory test by calibrating vehicles' ECTs so that their effectiveness is only ensured within the boundary conditions of the NEDC test. The discrepancies were generally not attributed to the possible use of prohibited defeat devices.

**E80.** Dieselgate, *Bundestag_Abgas_Untersuchungsausschuss_Report_Drs18-12900_2017_DE*, p. 348 ≈

> Es gab immer die entsprechende behördliche Antwort: Wir sehen das als eine legale Interpretation der Prüfvorschriften an, und das ist kein Beweis und kein Grund für ein entsprechendes Einschreiten. […] Das Problem war nun einfach, dass - egal was wir präsentiert haben und wie sehr wir auch in die Tiefe gegangen sind mit unseren Messungen und Erkenntnissen oder auch dem Hinweis auf Whistleblower – dies jeweils dargestellt wurde als ein legales, legitimes Handeln.

**E81.** Dieselgate, *EuroParl_EMIS_Inquiry_Final_Report_A8-0049-2017*, p. 37 ≈

> Defeat devices were generally not considered among the possible reasons behind the discrepancies between NOx emissions from diesel cars measured in the laboratory and measured on the road, because it was believed that these discrepancies could be sufficiently explained by the fact that the NEDC laboratory test was not representative of real driving, and that manufacturers could optimise their vehicles in order to pass the test cycle while apparently complying with the letter of EU law. It was no…

**E82.** Enron, *Senate_PSI_Role_of_Board_in_Enrons_Collapse_2002*, p. 49

> The October 2001 meeting was also when the Directors first learned of the Watkins' letter, although she was never identified by name to the Board, no Board member requested her identity, and the letter's strong warnings about the Raptors apparently were not disclosed to the outside directors. The interviewed directors said that Enron officers referred to the letter during the Board meeting as coming from an anonymous employee. They said it was discussed during an Audit Committee meeting first an…

**E83.** Enron, *Senate_PSI_Role_of_Board_in_Enrons_Collapse_2002*, p. 49

> The company's outside legal counsel, Vinson & Elkins, made the primary presentations and indicated that their preliminary investigation of the employee's concerns had found nothing worth further investigation.

**E84.** Enron, *House_EC_Hearing_Pt3_Watkins_testimony_2002-02-14*, p. 6

> Not surprisingly, the report that Vinson & Elkins issued on October 15 was so flawed that Ms. Watkins seriously considered leaving the company. Instead, she persisted in her attempts to convince Mr. Lay of the enormity of the challenge facing Enron and the failure of outside experts to clearly state the facts.

**E85.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo* ≈

> A Ford engineer, who doesn't want his name used, comments: "This company is run by salesmen, not engineers; so the priority is styling, not safety." He goes on to tell a story about gas-tank safety at Ford: Lou Tubben is one of the most popular engineers at Ford. He's a friendly, outgoing guy with a genuine concern for safety. By 1971 he had grown so concerned about gas-tank integrity that he asked his boss if he could prepare a presentation on safer tank design. Tubben and his boss had both wor…

**E86.** Ford Pinto, *Grimshaw_v_Ford_Motor_Co_1981_CalCtApp_119CalApp3d757*, p. 778

> In these conversations, both men expressed concern about the integrity of the Pinto's fuel system and complained about management's unwillingness to deviate from the design if the change would cost money.

**E87.** Ford Pinto, *Grimshaw_v_Ford_Motor_Co_1981_CalCtApp_119CalApp3d757*, p. 813

> vice president Harold MacDonald, who chaired the product review meetings, was present at one of those meetings at which a report on the crash tests was considered and a decision was made to defer corrective action

**E88.** Purdue OxyContin, *House_Oversight_Supplemental_Staff_Memo_2020-12-14*, p. 3 ≈

> Purdue executives and members of the Sackler family ignored safeguards from the company's Abuse and Diversion Detection program—intended to identify and cut off heath care providers suspected of suspicious prescribing behavior. Although members of the Sackler family were routinely informed of red flags raised by the program, many high-volume prescribers went unreported. Even in cases when they were reported, Purdue continued to deploy sales representatives to visit them.

**E89.** Purdue OxyContin, *DOJ_Purdue_Civil_Settlement_Agreement_2020-10*, p. 49

> However, high-volume prescribers were often not reported and, even if they were, they were sometimes not added to Region Zero until they lost the ability to prescribe through legal or medical board action. In addition, certain Purdue policies resulted in high-volume prescribers not being reported to ADD, and thus not being added to Region Zero. For example, Purdue trained its sales representatives to only report clear instances of abuse and diversion, and sales representatives were instructed to…

**E90.** Purdue OxyContin, *Purdue_Plea_Agreement_2020-10-20*, p. 73

> Although the analyses identified many red flag prescribers, only a fraction were reviewed as part of the ADD program and Purdue knowingly continued detailing others without any further scrutiny.

**E91.** Boeing 737MAX, *House_TI_Hearing_FAA_Oversight_Pierson_testimony_2019-12-11*, p. 6

> In November 2018, a few days after a powerful system running in the background of the 737 MAX called MCAS pushed Lion Air flight 610 into an unrecoverable dive, the FAA issued an emergency airworthiness directive that purported to inform pilots on how to respond to an erroneous activation of MCAS, while it actually never mentioned that system by name. In fact, during the certification of the 737 MAX, Boeing actively pushed the FAA to remove references to MCAS from the flight crew operating manua…

**E92.** Boeing 737MAX, *SEC_Order_Muilenburg_33-11106_2022-09-22*, p. 7

> On or about November 15, 2018, Boeing safety engineers concluded that, in light of the SRB's findings, the MCAS software should be redesigned and re-installed on the 737 MAX fleet to remediate the high crew workload "airplane safety issue." They determined that the software redesign had to be completed within approximately 27 months, but that the 737 MAX fleet could continue to operate in the interim in light of Boeing's bulletin and the FAA emergency airworthiness directive.

**E93.** Boeing 737MAX, *Boeing_Non-Prosecution_Agreement_2025-05-29*, p. 31

> Despite knowing that the FAA AEG had issued its provisional "Level B" determination without any awareness that MCAS's operational scope had been expanded to include high angle of attack conditions in nearly the entire speed range of ordinary commercial flight, Boeing Employee-1 and Boeing Employee-2 did not correct the FAA AEG's understanding of MCAS's operational scope or otherwise ensure that the FAA AEG's "Level B" determination was based on an accurate understanding of MCAS's operation. Inst…

**E94.** Dieselgate, *Winterkorn_et_al_Fifth_Superseding_Indictment*, p. 24 ≈

> When U.S. regulators threatened not to certify VW model year 2016 vehicles for sale in the United States, WINTERKORN requested a briefing on the situation in the United States. On or about July 27, 2015, VW employees presented to WINTERKORN, NEUSSER, and other senior VW AG management at an in-person meeting at VW's headquarters in Wolfsburg. VW AG employees used a PowerPoint presentation to provide to WINTERKORN a clear picture of: (1) how VW was deceiving U.S. regulators, including precisely wh…

**E95.** Dieselgate, *Winterkorn_et_al_Fifth_Superseding_Indictment*, p. 25 ≈

> On or about August 19, 2015, in a meeting with CARB in El Monte, California, in contravention of instructions from WINTERKORN, and despite a specific script for the meeting approved by NEUSSER and others, a VW employee explained that certain of the 2.0 Liter Subject Vehicles used different emissions treatment depending on whether the vehicles were on the dynamometer or the road, thereby signaling that VW had cheated on U.S. emissions tests. The August 19, 2015, meeting was the first time a VW em…

**E96.** Dieselgate, *Winterkorn_et_al_Fifth_Superseding_Indictment*, p. 24

> Throughout 2014 and the first half of 2015, NEUSSER, GOTTWEIS, PETER, WINTERKORN, and their co-conspirators, continued to offer, and cause to be offered, software and hardware "fixes" and explanations to U.S. regulators for the 2.0 Liter Subject Vehicles' higher NOx measurements on the road without revealing the underlying reason - the existence of software designed to detect, evade and defeat U.S. emissions tests.

**E97.** Enron, *Causey_Indictment_2004*, p. 7

> For example, in the fourth quarter of 2000, under the direction of CAUSEY and others, Enron personnel fraudulently increased the value of one of the largest of Enron's merchant assets, Mariner Energy, by $100 million in order to help close a budget gap.

**E98.** Enron, *Powers_Report_Special_Investigative_Committee_2002-02-01*, p. 14

> Rather than take that loss, Enron "restructured" the Raptor vehicles by, among other things, transferring more than $800 million of contracts to receive its own stock to them just before quarter-end. This transaction apparently was not disclosed to or authorized by the Board, involved a transfer of very substantial value for insufficient consideration, and appears inconsistent with governing accounting rules. It continued the concealment of the substantial losses in Enron's merchant investments.

**E99.** Enron, *House_EC_Hearing_Pt1_Powers_testimony_2002-02-05*, p. 21

> By March 2001, it appeared that Enron would be required to take a charge against earnings of more than $500 million to reflect the inability of the Raptors to pay. But then rather than take that loss, Enron compounded the problem by making even more of its own stock available to the Raptors—$800 million worth. It gave the false impression that the Raptors had enough money to pay Enron on the money it owed, on the money that the Raptors owed. This transaction was apparently hidden from the board,…

**E100.** Ford Pinto, *Grimshaw_v_Ford_Motor_Co_1981_CalCtApp_119CalApp3d757*, p. 813

> Through the results of the crash tests Ford knew that the Pinto's fuel tank and rear structure would expose consumers to serious injury or death in a 20- to 30-mile-per-hour collision. There was evidence that Ford could have corrected the hazardous design defects at minimal cost but decided to defer correction of the shortcomings by engaging in a cost-benefit analysis balancing human lives and limbs against corporate profits.

**E101.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> Ford picked portions of Standard 301 for strong opposition way back in 1968 when the Pinto was still in the blueprint stage. The intent of 301, and the 300 series that followed it, was to protect drivers and passengers after a crash occurs. Without question the worst post-crash hazard is fire. So Standard 301 originally proposed that all cars should be able to withstand a fixed barrier impact of 20 mph (that is, running into a wall at that speed) without losing fuel. When the standard was propos…

**E102.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> Not long after the government arrived at the $200,725-per-life figure, it surfaced, rounded off to a cleaner $200,000, in an internal Ford memorandum. This cost-benefit analysis argued that Ford should not make an $11-per-car improvement that would prevent 180 fiery deaths a year. (This minor change would have prevented gas tanks from breaking so easily both in rear-end collisions, like Sandra Gillespie's, and in rollover accidents, where the same thing tends to happen.)

**E103.** Purdue OxyContin, *Massachusetts_AG_First_Amended_Complaint_Purdue_Sacklers_2019-01-31*, p. 82

> In October, staff told the Sacklers that surveillance data monitored by Purdue indicated a "wide geographic dispersion" of abuse and diversion of OxyContin "throughout the United States." Staff told the Sacklers that "availability of the product" and "prescribing practices" were key factors driving abuse and diversion of OxyContin." On the same day, staff told the Sacklers that Purdue had begun a new "Toppers Club sales contest" for sales reps to win bonuses, based on how much a rep increased Ox…

**E104.** Purdue OxyContin, *Purdue_Criminal_Information_DNJ_2020-11-24*, p. 11

> PURDUE PHARMA received additional, direct evidence that many of its Region Zero Prescribers were in fact actively engaged in diversion when it introduced an abuse-deterrent reformulation of OxyContin ("ADF OxyContin") in 2010. ADF OxyContin was designed to be more difficult to crush, and therefore more difficult to abuse. Shortly after ADF OxyContin's release, PURDUE PHARMA's internal analyses showed a two-thirds decrease in prescriptions written by Region Zero Prescribers, thus directly linking…

**E105.** Purdue OxyContin, *House_Oversight_Supplemental_Staff_Memo_2020-12-14*, p. 3 ≈

> Documents obtained by DOJ show that from 2013 to 2018, Purdue—with the express approval of members of the Sackler family—engaged in a marketing initiative called "Evolve to Excellence" (E2E), developed in conjunction with the consulting firm McKinsey & Company, to intensify marketing to the highest-volume opioid prescribers and target them with increased frequency. Purdue representatives, whose compensation was tied to sales volume, encouraged high-volume prescribers to prescribe more of Purdue'…

**E106.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 107

> Lion Air flight 610 crashes 13 minutes after takeoff killing 189 people. MCAS is quickly determined to be a major factor in the crash. Faulty AOA data erroneously caused MCAS to repetitively activate more than 20 times as the pilots battled MCAS for control of the aircraft.

**E107.** Boeing 737MAX, *FAA_737MAX_Return_to_Service_Summary_2020-11*, p. 19 ≈

> On March 10, 2019, ET302 crashed shortly after takeoff in Addis Ababa, Ethiopia. Partial data (e.g., altitude, airspeed and vertical speed) was available from a land-based Automatic Dependent Surveillance—Broadcast (ADS-B) system. On March 11, 2019, the FAA issued another CANIC (see Appendix D) indicating the FAA was actively involved in supporting the investigations. On March 11, the FAA received additional ADS-B data. The data was analyzed and reviewed on March 12 and through the early hours o…

**E108.** Boeing 737MAX, *SEC_Order_Boeing_33-11105_2022-09-22*, p. 7 ≈

> The Lion Air Crash occurred on October 29, 2018. Soon after the crash, investigators identified repeated unintended activations of MCAS triggered by erroneous AoA data as a cause of the accident. In the weeks following the Lion Air Crash, Boeing convened a series of meetings of its Safety Review Board ("SRB") – an internal body comprised of Boeing personnel that evaluate in-service aircraft safety issues – on November 4, 2018, November 6, 2018, and November 15, 2018, to assess the ongoing safety…

**E109.** Dieselgate, *Dorenkamp_et_al_Second_Superseding_Indictment*, p. 21 ≈

> In or around March 2014, certain VW employees, including NEUSSER, GOTTWEIS, SCHMIDT, and PETER learned of the results of a study undertaken by West Virginia University's Center for Alternative Fuels, Engines and Emissions and commissioned by the International Council on Clean Transportation (the "ICCT study"). The ICCT study identified substantial discrepancies in the NOx emissions from certain 2.0 Liter Subject Vehicles when tested on the road compared to when these vehicles were undergoing EPA…

**E110.** Dieselgate, *Winterkorn_et_al_Fifth_Superseding_Indictment*, p. 22

> Upon learning of the negative results of the ICCT study, VW engineers informed VW senior managemen t of the risk that the study would reveal VW's cheating. Specifically, on or about April 28, 2014, engineers in VW's Brand Engine Developme nt department met with GOTTWEIS and briefed him on the ICCT study, how VW was cheating, and on the consequenc es of that study, including that VW may have to buy back 500,000 vehicles sold in the United States.

**E111.** Dieselgate, *House_EC_Majority_Staff_Hearing_Memo_2015-10-06*, p. 6 ≈

> September 23, 2015: Dr. Winterkorn resigned from VW. September 25, 2015: VW suspended the leaders of the VW, Audi, and Porsche research and development divisions and announced a restructuring of its North American business unit.

**E112.** Enron, *Senate_Financial_Oversight_of_Enron_SEC_Watchdogs_2002*, p. 90

> On October 17, The Wall Street Journal broke the story about partnerships run by Enron CFO Andrew Fastow being used to hide Enron losses and debt.

**E113.** Enron, *Senate_PSI_Role_of_Board_in_Enrons_Collapse_2002*, p. 17

> But the company was not on track. In mid-October 2001, press reports began leaking Enron's extensive undisclosed off-the-books dealings with LJM and the millions of dollars Mr. Fastow had made at Enron's expense. Reports also emerged about Enron's dealings with JEDI and a previously undisclosed related company called Chewco which was owned and operated by another Enron employee Michael Kopper and which, due to improper accounting years earlier, Enron had to consolidate on its books in 2001, with…

**E114.** Enron, *House_EC_Hearing_Pt2_Skilling_testimony_2002-02-07*, p. 108 ≈

> On October 16, 2001, Enron announced that it was taking a $544 million after-tax charge against earnings related to transactions with LJM2, a partnership created and managed by Enron's CFO, Andrew Fastow. On the same day Ken Lay announced at an analysts' meeting that, in connection with the same transactions, it would take a $1.2 billion non-cash reduction to shareholder equity. Two weeks later, in order to learn how these losses had been incurred, the Board of Enron Corp. appointed a Special In…

**E115.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> While government bureaucrats dragged their feet on lifesaving Standard 301, a different kind of expert was taking a close look at the Pinto—the "recon man." "Recon" stands for reconstruction; recon men reconstruct accidents for police departments, insurance companies and lawyers who want to know exactly who or what caused an accident. It didn't take many rear-end Pinto accidents to demonstrate the weakness of the car. Recon men began encouraging lawyers to look beyond one driver or another to th…

**E116.** Ford Pinto, *NHTSA_News_Releases_Aug-Dec_1977*, p. 48 ≈

> In response to recent charges about the safety of Ford Pinto gas tanks in rear-end collisions, the department's National Highway Traffic Safety Administration (NHTSA) has begun a special program of vehicle-to-vehicle crash testing to measure the susceptibility to fire of fuel tanks in Pintos and other small cars. NHTSA Administrator Joan Claybrook said the agency also will test full sized vehicles to establish a baseline for comparative purposes.

**E117.** Ford Pinto, *NHTSA_News_Releases_Jan-Jun_1978*, p. 117 ≈

> The U.S. Departmen t of Transporta tion announced today that it has made an initial determinat ion that a safety defect exists in the fuel systems of some 1. 9 million Ford Pinto and 30, 000 Mercury model years (except station wagons). An investigatio n conducted by the departmen t's National Highway Traffic Safety Administra tion (NHTSA), on the crash performanc e of the Pinto'' s fuel tank and filler pipe has been completed. The findings of this investigatio n demonstrat e that low to moderate…

**E118.** Purdue OxyContin, *Senate_Judiciary_Brownlee_Testimony_2007-07-31*, p. 2

> In response to the effects of OxyContin abuse and diversion, government officials and private citizens began focusing on Purdue and OxyContin. Product liability litigation began in Ohio in April, 2001.

**E119.** Purdue OxyContin, *House_Oversight_Supplemental_Staff_Memo_2020-12-14*, p. 2 ≈

> In 2007, following a four-year investigation into Purdue's marketing practices, the Department of Justice (DOJ) settled with Purdue Pharma's parent company, the Purdue Frederick Company, and three of Purdue's top executives on charges of "misbranding"—reportedly over the objection of federal prosecutors who recommended bringing felony charges, including conspiracy to defraud, against the executives. Purdue paid $600 million in fines, and the settlement did not include any admission of liability …

**E120.** Purdue OxyContin, *SCOTUS_Harrington_v_Purdue_Pharma_Opinion_2024-06-27*, p. 7 ≈

> Eventually, however, the firm came under scrutiny. In 2007, a Purdue affiliate pleaded guilty to a federal felony for misbranding OxyContin as 'less addictive' and 'less subject to abuse than other pain medications.' Thousands of civil lawsuits followed as individuals, families, and governments within and outside the United States sought damages from Purdue and the Sacklers for injuries allegedly caused by their deceptive marketing practices.
