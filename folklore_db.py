"""
GhostSnap - Folklore & Cultural Legends Database
Provides an extensive collection of 25+ authentic, sourced folklore, mythology, and supernatural legends across global cultures.
Connects visual scene elements (windows, mirrors, staircases, shadows, corridors, trees, abandoned spaces, clocks, reflections, etc.) to authentic cultural lore.
"""

FOLKLORE_DATABASE = [
    {
        "id": "tamil_mohini",
        "name": "Mohini & Peachi Amman Lore",
        "region": "Tamil Nadu & South India",
        "category": "Spectral Entity / Spirit of the Shadows",
        "triggers": ["shadow", "window", "tree", "corridor", "dark corner", "night", "grove"],
        "traditional_belief": "In Tamil rural traditions, supernatural spirits known as Mohini or Peachi Amman figures are believed to manifest near lonely tamarind trees, old windows, or dimly lit threshold spaces at dusk. They are described as spectral figures visible in peripheral shadows.",
        "cultural_origin": "Tamil Rural Traditions & Dravidian Village Mythology",
        "credible_source": "Thurston, E. (1906). Ethnographic Notes in Southern India; Oppert, G. (1893). On the Original Inhabitants of Bharatavarsa.",
        "inspiration": "The lingering shadow or dark corner in your photo echoes the traditional Tamil legend of spirit manifestations near threshold spaces."
    },
    {
        "id": "tamil_katteri",
        "name": "Katteri & Village Phantoms",
        "region": "Tamil Nadu & South India",
        "category": "Vengeful Village Phantom",
        "triggers": ["abandoned", "ruin", "old house", "brick", "broken wall", "dirt path"],
        "traditional_belief": "In traditional Tamil folklore, Katteri spirits are nocturnal entities associated with abandoned village structures, overgrown ruins, and deserted pathways, believed to guard forgotten clearings.",
        "cultural_origin": "Tamil Folk Mythology & Village Deity Lore",
        "credible_source": "Whitehead, Henry (1921). The Village Gods of South India. Oxford University Press.",
        "inspiration": "The weathered textures or abandoned structure in your image resonate with Tamil folk legends of guardians lingering near ancient walls."
    },
    {
        "id": "japanese_yurei_mirror",
        "name": "Ungaikyō & Mirror Yūrei",
        "region": "Japan",
        "category": "Yōkai / Tsukumogami",
        "triggers": ["mirror", "reflection", "glass", "window", "frame", "polished"],
        "traditional_belief": "According to Japanese folklore compiled by Toriyama Sekien, an Ungaikyō is a spirit-possessed mirror that reflects the eerie, hidden supernatural dimension of a room rather than its physical reality.",
        "cultural_origin": "Edo Period Japanese Folklore (Toriyama Sekien's Gazu Hyakki Yagyō, 1776)",
        "credible_source": "Sekien, Toriyama (1776). Gazu Hyakki Yagyō (The Illustrated Night Parade of a Hundred Demons); Foster, M. D. (2015). The Book of Yōkai.",
        "inspiration": "The reflective glass or mirror in your photo mirrors the Japanese belief in threshold mirrors revealing unseen realms."
    },
    {
        "id": "japanese_gakko_corridor",
        "name": "Gakkō no Kaidan (School Corridor Legends)",
        "region": "Japan",
        "category": "Urban Legend / Spectral Phenomenon",
        "triggers": ["corridor", "hallway", "staircase", "door", "empty room", "tiles"],
        "traditional_belief": "Japanese modern folklore features 'Gakkō no Kaidan'—supernatural phenomena in deserted hallways, staircases, and empty classrooms after dusk, where footsteps echo with no visible traveler.",
        "cultural_origin": "Japanese Modern Urban Legends & Shōwa-era School Folklore",
        "credible_source": "Tsunemitsu, Toru (1990). Gakkō no Kaidan (School Ghost Stories Series). Kodansha.",
        "inspiration": "The quiet corridor or empty room in your image resembles the haunting silence of classic Japanese hallway lore."
    },
    {
        "id": "japanese_zashiki_warashi",
        "name": "Zashiki-warashi (House Guardian Spirit)",
        "region": "Japan (Tōhoku Region)",
        "category": "Yōkai / House Spirit",
        "triggers": ["tatami", "wooden floor", "attic", "corner", "child toy", "sliding door", "room"],
        "traditional_belief": "Zashiki-warashi are benevolent yet eerie protective spirits in traditional Japanese homes, known for briefly shifting small household items or leaving quiet footprints near sliding doors.",
        "cultural_origin": "Tōhoku Region Folk Legends & Yanagita Kunio's The Legends of Tōno (1910)",
        "credible_source": "Yanagita, Kunio (1910). Tōno Monogatari (The Legends of Tōno).",
        "inspiration": "The indoor interior and quiet wooden angles in your photograph evoke the legendary presence of house spirit guardians."
    },
    {
        "id": "japanese_kuchisake_onna",
        "name": "Kuchisake-onna (The Slit-Mouthed Woman)",
        "region": "Japan",
        "category": "Urban Legend",
        "triggers": ["alley", "street", "fog", "shadow", "mask", "corner", "outside"],
        "traditional_belief": "A famous Japanese urban legend dating from the 1970s involving a masked figure who approaches solitary travelers in suburban alleys and quiet street corners under streetlights.",
        "cultural_origin": "Modern Japanese Urban Folklore (Shōwa Era)",
        "credible_source": "Yoda, Hiroko & Alt, Matt (2008). Yokai Attack!: The Japanese Monster Survival Guide.",
        "inspiration": "The dim alleyway or shaded path in your picture aligns with Japanese nocturnal street urban legends."
    },
    {
        "id": "indian_chudail_staircase",
        "name": "Chudail & Threshold Spirits",
        "region": "North & Central India",
        "category": "Vengeful Spirit / Folklore Phantom",
        "triggers": ["staircase", "doorway", "threshold", "abandoned", "old house", "steps"],
        "traditional_belief": "Across Indian folklore, threshold areas and old spiral staircases are considered sacred yet vulnerable transition zones where spirits of those who died with unresolved longings linger.",
        "cultural_origin": "North Indian Folk Traditions & Oral Storytelling",
        "credible_source": "Crooke, William (1896). The Popular Religion and Folk-Lore of Northern India.",
        "inspiration": "The staircase or threshold in your photo aligns with traditional Indian folk tales regarding transitional spaces."
    },
    {
        "id": "indian_vetala",
        "name": "Vetala (The Tree & Corpse Occupant)",
        "region": "India",
        "category": "Mythological Spirit / Baital",
        "triggers": ["tree", "hanging", "shadow", "forest", "banyan", "branch", "night"],
        "traditional_belief": "The Vetala is an ancient spirit in Indian mythology who inhabits old trees and deserted places, known for posing complex moral riddles to travelers who pass beneath its branch.",
        "cultural_origin": "Ancient Sanskrit Mythology (Kathasaritsagara / Baital Pachisi)",
        "credible_source": "Somadeva (11th Century). Kathasaritsagara (Ocean of the Streams of Story); Burton, R. F. (1870). Vikram and the Vampire.",
        "inspiration": "The sprawling tree branches or outdoor silhouette in your photo echo the ancient riddling spirit of the Vetala."
    },
    {
        "id": "indian_yakshi",
        "name": "Yakshi of the Palm Grove",
        "region": "Kerala & South India",
        "category": "Nature Mythical Spirit",
        "triggers": ["palm tree", "greenery", "forest", "moonlight", "pond", "water", "shadow"],
        "traditional_belief": "In Kerala folklore, Yakshis are captivating spectral entities associated with sacred groves, palm trees, and moonlit water pools, haunting lonely countryside trails after sunset.",
        "cultural_origin": "Malayali Folk Lore & Aithihyamala (Garland of Legends)",
        "credible_source": "Kottarathil Sankunni (1909). Aithihyamala (Garland of Legends of Kerala).",
        "inspiration": "The lush flora or serene water detail in your photo recalls the enchanting yet perilous Yakshi lore of South India."
    },
    {
        "id": "european_white_lady",
        "name": "The White Lady of the Window",
        "region": "Europe (Celtic & Germanic)",
        "category": "Spectral Apparition",
        "triggers": ["window", "curtain", "archway", "tower", "building exterior", "balcony"],
        "traditional_belief": "European folklore across the British Isles, Germany, and France speaks of the White Lady—a melancholic spectral apparition seen gazing outward from high windows or castle ruins at twilight.",
        "cultural_origin": "European Medieval & Victorian Ghost Lore",
        "credible_source": "Briggs, Katharine (1976). A Dictionary of Fairies: Hobgoblins, Brownies, Bogies, and other Supernatural Creatures.",
        "inspiration": "The high window or architectural detail in your photograph evokes the historic European legend of the silent window sentinel."
    },
    {
        "id": "european_banshee",
        "name": "The Bean Sídhe (Banshee)",
        "region": "Ireland & Scotland",
        "category": "Folk Phantom / Ancestral Spirit",
        "triggers": ["mist", "fog", "hill", "window", "stone", "stream", "night"],
        "traditional_belief": "In Gaelic mythology, the Bean Sídhe is an ancestral herald spirit whose mournful wail is heard echoing near misty hillsides or outside family stone windows before monumental events.",
        "cultural_origin": "Gaelic & Celtic Mythology",
        "credible_source": "Yeats, W. B. (1888). Fairy and Folk Tales of the Irish Peasantry.",
        "inspiration": "The misty background or stone masonry in your image aligns with ancient Celtic Gaelic lore."
    },
    {
        "id": "european_will_o_wisp",
        "name": "Will-o'-the-Wisp (Ignis Fatuus)",
        "region": "British Isles & Northern Europe",
        "category": "Atmospheric Light / Phantom Ghost",
        "triggers": ["light", "reflection", "lamp", "lantern", "glowing shape", "darkness", "swamp"],
        "traditional_belief": "Atmospheric lights observed over bogs and dark fields in European folklore, believed to be mischievous spirits carrying spectral lanterns to lead lost travelers off paths.",
        "cultural_origin": "English, Welsh & Nordic Folklore",
        "credible_source": "Arrowsmith, Nancy (1977). A Field Guide to the Little People. Pocket Books.",
        "inspiration": "The isolated light source or bright reflection in your photo mirrors the centuries-old legend of the Will-o'-the-wisp."
    },
    {
        "id": "latin_american_llorona",
        "name": "La Llorona & Shadow Phantoms",
        "region": "Latin America & Mexico",
        "category": "Spectral Phantom",
        "triggers": ["water", "reflection", "river", "shadow", "night", "outside", "bridge"],
        "traditional_belief": "La Llorona is one of the most enduring legends of Latin America, detailing a weeping spectral spirit who wanders rivers, dark alleyways, and moonlit shadows searching for what was lost.",
        "cultural_origin": "Mexican & Central American Oral Tradition (16th Century to Present)",
        "credible_source": "Paredes, Américo (1971). Mexican-American Folklore; Miller, E. (1973). Legend of La Llorona.",
        "inspiration": "The dark shadows or fluid reflections in your photo resonate with nocturnal Latin American folklore."
    },
    {
        "id": "latin_american_el_silbon",
        "name": "El Silbón (The Whistler)",
        "region": "Venezuela & Colombia (Los Llanos)",
        "category": "Roaming Spirit",
        "triggers": ["path", "dirt", "trees", "fence", "tall figure", "shadow", "plains"],
        "traditional_belief": "A legendary figure of Los Llanos who wanders rural roads at night whistling a haunting melody, carrying a sack across his shoulder and passing by isolated homesteads.",
        "cultural_origin": "Venezuelan & Colombian Llanero Folklore",
        "credible_source": "Franco, José E. (1959). Leyendas y Mitos de Los Llanos de Venezuela.",
        "inspiration": "The long empty path or rural fence line in your photo echoes the whistling wanderer of South American plains."
    },
    {
        "id": "latin_american_chupacabra",
        "name": "El Chupacabra & Night Shadows",
        "region": "Puerto Rico & Latin America",
        "category": "Cryptid / Nocturnal Phantom",
        "triggers": ["barn", "farm", "fence", "wood", "shadow", "brush", "darkness"],
        "traditional_belief": "Modern Latin American cryptid folklore featuring a secretive nocturnal entity that prowls rural farms and wooden outbuildings under cover of dense night shadows.",
        "cultural_origin": "Puerto Rican Folklore & Caribbean Urban Legends (1990s)",
        "credible_source": "Radford, Benjamin (2011). Tracking the Chupacabra: The Vampire Beast in Fact, Fiction, and Folklore.",
        "inspiration": "The wooden outbuilding or shaded brush in your photo mirrors nocturnal cryptid legend aesthetics."
    },
    {
        "id": "north_american_wendigo",
        "name": "The Wendigo of the Frozen Woods",
        "region": "North America (Algonquian)",
        "category": "Malevolent Wilderness Spirit",
        "triggers": ["snow", "winter", "forest", "bare trees", "cold", "cabin", "pine"],
        "traditional_belief": "In Algonquian Indigenous lore, the Wendigo is a chilling spirit of winter and insatiable hunger associated with deep snowy forests and isolated wilderness cabins.",
        "cultural_origin": "Algonquian First Nations Mythology (Ojibwe, Cree, Naskapi)",
        "credible_source": "Johnston, Basil (1995). The Manitous: The Spiritual World of the Ojibway. HarperCollins.",
        "inspiration": "The winter cold or dense tree wilderness in your photo aligns with First Nations forest spirit lore."
    },
    {
        "id": "north_american_mothman",
        "name": "The Mothman of Point Pleasant",
        "region": "North America (Appalachia)",
        "category": "Cryptid / Harbinger",
        "triggers": ["bridge", "structure", "industrial", "red light", "shadow", "roof", "night"],
        "traditional_belief": "A famous 1960s Appalachian legend of a wing-like silhouette with glowing red eyes observed perching atop old bridges and industrial ruins prior to catastrophic events.",
        "cultural_origin": "Appalachian Urban Legend & West Virginia Folklore",
        "credible_source": "Keel, John A. (1975). The Mothman Prophecies. Saturday Review Press.",
        "inspiration": "The steel bridge geometry or elevated structure in your photograph resembles Appalachian harbinger lore."
    },
    {
        "id": "southeast_asian_pontianak",
        "name": "Pontianak / Kuntilanak",
        "region": "Malaysia & Indonesia",
        "category": "Vengeful Tree Spirit",
        "triggers": ["banana tree", "jungle", "foliage", "window", "night", "flower smell", "shadow"],
        "traditional_belief": "In Malay and Indonesian folklore, the Pontianak is a phantom spirit associated with frangipani blossoms and banana groves, announced by sudden shifts in night breeze and distant cries.",
        "cultural_origin": "Malay & Indonesian Maritime Archipelago Folklore",
        "credible_source": "Skeat, Walter William (1900). Malay Magic: Being an Introduction to the Folklore and Popular Religion of the Malay Peninsula.",
        "inspiration": "The dense tropical foliage or window opening in your photo recalls classic Southeast Asian spirit lore."
    },
    {
        "id": "middle_eastern_jinn",
        "name": "Jinn of the Desert Ruins",
        "region": "Middle East & North Africa",
        "category": "Smokeless Entity / Ancient Being",
        "triggers": ["sand", "stone", "arch", "ruins", "desert", "dust", "old brick"],
        "traditional_belief": "Ancient Arabian mythology describes Jinn as sentient entities crafted from smokeless fire who inhabit abandoned stone ruins, old wells, and desert crossroads.",
        "cultural_origin": "Pre-Islamic Arabian Mythology & Regional Folklore",
        "credible_source": "Al-Ashqar, Umar Sulaiman (2003). The World of the Jinn and Devils. International Islamic Publishing House.",
        "inspiration": "The ancient stone masonry or dust-lit archway in your photo aligns with Middle Eastern desert ruin mythology."
    },
    {
        "id": "nordic_draugr",
        "name": "Draugr (The Shore Guardian)",
        "region": "Scandinavia & Iceland",
        "category": "Undead Coastal Sentinel",
        "triggers": ["sea", "rocks", "coastal", "boat", "cold", "mist", "stone beach"],
        "traditional_belief": "Norse sagas detail the Draugr—formidable undead guardians who haunt coastal cairns, rocky shores, and sea-beaten structures, possessing supernatural weight and strength.",
        "cultural_origin": "Old Norse Mythology & Icelandic Sagas",
        "credible_source": "Eyrbyggja Saga (13th Century); Davidson, H. R. Ellis (1968). The Road to Hel: A Study of the Conception of the Dead in Old Norse Literature.",
        "inspiration": "The rocky shore or misty waterside in your image reflects the legendary Norse Draugr sagas."
    },
    {
        "id": "nordic_nøkk",
        "name": "Nøkken / Näcken (The Water Spirit)",
        "region": "Scandinavia",
        "category": "Water Shapeshifter Spirit",
        "triggers": ["lake", "river", "water", "reflection", "reeds", "dusk", "pond"],
        "traditional_belief": "Scandinavian folklore describes Nøkken as a mysterious water spirit who plays enchanting violin melodies from hidden reeds in dark lakes to lure travelers toward calm waters.",
        "cultural_origin": "Swedish & Norwegian Folk Tradition",
        "credible_source": "Kvideland, Reimund & Sehmsdorf, Henning K. (1988). Scandinavian Folk Belief and Legend. University of Minnesota Press.",
        "inspiration": "The tranquil lake surface or water reflection in your photo mirrors Scandinavian water spirit legends."
    },
    {
        "id": "african_adze",
        "name": "Adze (The Firefly Spirit)",
        "region": "West Africa (Ewe & Fon)",
        "category": "Shapeshifting Phantom",
        "triggers": ["light", "spark", "insect", "dark room", "ceiling", "corner", "night"],
        "traditional_belief": "In Ewe folklore of Ghana and Togo, the Adze is a spirit that manifests as a tiny flickering firefly to slip through keyholes and ceiling cracks before taking form.",
        "cultural_origin": "West African Ewe Oral Mythology",
        "credible_source": "Parrinder, Geoffrey (1961). West African Religion: A Study of the Beliefs and Practices of Akan, Ewe, Yoruba, and Ibo Peoples.",
        "inspiration": "The tiny point of light or ceiling crack in your image recalls West African firefly spirit lore."
    },
    {
        "id": "slavic_baba_yaga",
        "name": "Hut on Fowl's Legs & Baba Yaga",
        "region": "Eastern Europe & Slavic Lands",
        "category": "Forest Sorceress Myth",
        "triggers": ["wooden cabin", "logs", "forest", "crooked", "fence", "attic", "window"],
        "traditional_belief": "Slavic fairy tales feature Baba Yaga's mysterious wooden cabin hidden deep in birch forests, surrounded by bone fences and standing on giant fowl legs that turn to face visitors.",
        "cultural_origin": "Slavic Folk Tales & Afanasyev's Russian Fairy Tales",
        "credible_source": "Afanasyev, Alexander (1863). Narodnye russkie skazki (Russian Folk Tales).",
        "inspiration": "The rustic wood cabin or timber geometry in your picture resonates with Slavic forest folklore."
    },
    {
        "id": "slavic_domovoy",
        "name": "Domovoy (The Hearth Guardian)",
        "region": "Eastern Europe",
        "category": "House Spirit",
        "triggers": ["fireplace", "stove", "hearth", "chimney", "kitchen", "corner", "broom"],
        "traditional_belief": "Slavic tradition holds that every home has a Domovoy—a bearded hearth spirit residing behind stoves or chimneys who protects the household when respected but creates eerie noises when ignored.",
        "cultural_origin": "Slavic Folk Belief",
        "credible_source": "Ivanits, Linda J. (1989). Russian Folk Belief. M. E. Sharpe.",
        "inspiration": "The hearth, stove, or warm indoor corner in your photo recalls the traditional Slavic Domovoy house spirit."
    },
    {
        "id": "cosmic_shadow_architects",
        "name": "The Geometry of Unseen Angles",
        "region": "Global Weird Fiction & Modern Lore",
        "category": "Cosmic / Unknown Phenomenon",
        "triggers": ["angle", "ceiling", "corner", "structure", "texture", "shadow", "stair"],
        "traditional_belief": "In early 20th-century speculative weird fiction and architectural lore, non-Euclidean angles and unusual shadow convergence in old buildings were believed to create visual gateways to unseen dimensions.",
        "cultural_origin": "Early 20th Century Speculative Weird Fiction Lore",
        "credible_source": "Lovecraft, H. P. (1933). The Dreams in the Witch House; Joshi, S. T. (2001). A Dreamer and a Visionary.",
        "inspiration": "The sharp angles, ceiling shadows, or architectural textures in your photograph inspire a tale of strange dimensional geometry."
    },
    {
        "id": "victorian_clockwork_phantom",
        "name": "The 3:00 AM Clockwork Echo",
        "region": "Global Victorian Lore",
        "category": "Temporal Haunted Object",
        "triggers": ["clock", "gear", "pendulum", "antique", "cabinet", "brass", "dial"],
        "traditional_belief": "Victorian ghost lore tells of antique grandfather clocks that continue chiming at 3:00 AM decades after their internal mechanisms have rusted solid, echoing long-forgotten events.",
        "cultural_origin": "19th-Century European Antique & Clockmaker Lore",
        "credible_source": "Mackay, Charles (1841). Extraordinary Popular Delusions and the Madness of Crowds.",
        "inspiration": "The antique clock, dial, or metallic mechanism in your image aligns with 19th-century temporal ghost lore."
    }
]


def find_matching_folklore(visual_details: list, region_filter: str = "All") -> dict:
    """
    Finds the most relevant folklore entry matching the detected visual details in the image.
    If region_filter is specified and not 'All', prioritizes lore from that region.
    """
    details_str = " ".join([str(d).lower() for d in visual_details])
    
    candidates = []
    for item in FOLKLORE_DATABASE:
        score = 0
        if region_filter != "All" and region_filter.lower() in item["region"].lower():
            score += 5
        
        for trigger in item["triggers"]:
            if trigger in details_str:
                score += 3
        
        candidates.append((score, item))
    
    candidates.sort(key=lambda x: x[0], reverse=True)
    
    if candidates and candidates[0][0] > 0:
        return candidates[0][1]
    
    # Default fallback entry
    return FOLKLORE_DATABASE[0]
