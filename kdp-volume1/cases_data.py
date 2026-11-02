# -*- coding: utf-8 -*-
"""Dati dei 50 casi del Volume 1 (villaggio inventato: Marrowby).
Ogni caso: (titolo, ambientazione, storia, [3 indizi], PAROLA_INDIZIO, "15 parole ...")
La parola-indizio e' la 16a parola: nascosta nella griglia ma NON in lista.
Le iniziali delle 50 parole-indizio, lette in ordine, formano la frase finale (MESSAGE).
"""

MESSAGE = "THE CULPRIT IS TOBIAS FENN THE ANTIQUE DEALER WHO LIED TWICE"

CASES = [
("The Vicarage Tea", "The vicarage kitchen",
 "Reverend Quill welcomes you into the vicarage kitchen. Ambrose Wickes, the village clockmaker, was due for tea on the night he died, and the vicar has kept his place laid ever since. 'It was my mother's,' he sighs, 'and now it has vanished from the dresser.' You promise to find what is missing before the biscuits go cold.",
 ["Steam once curled from a chipped spout.", "A knitted cosy sits empty on the table.", "Four cups are set, yet nothing is left to pour from."],
 "TEAPOT", "BISCUIT SAUCER KETTLE SCONE MARMALADE DRESSER PULPIT HYMNAL CASSOCK SERMON CURATE PARISH LEMON SUGAR TRAY"),

("The Smithy's Secret", "The village forge",
 "The blacksmith mops his brow as you step into the forge. He saw Ambrose leave at dusk, carrying something small and lucky. 'I made it for a friend,' he says, 'and it was never paid for. Half the barn doors in the county wear one, you know.' Whoever took the second one left a trail of soot on the cobbles.",
 ["Seven nail holes, worn smooth.", "It is shaped like a letter U.", "Farmers nail it above the door for good luck."],
 "HORSESHOE", "ANVIL BELLOWS TONGS FURNACE SMITH HAMMER CHARCOAL SPARKS APPRENTICE QUENCH BRAZIER RIVET FORGE HEARTH MOLTEN"),

("The Letter Never Sent", "Marrowby Post Office",
 "Mabel Pennyfeather runs the post office and misses nothing. Ambrose came in on his last afternoon, bought a stamp, and wrote for ten minutes at her counter. 'He never posted it,' Mabel whispers. 'He tucked it into his coat and hurried out.' Somewhere in the village, it is still waiting to be opened.",
 ["Cream paper with a sticky flap.", "A name, but no stamp, on the front.", "A folded letter is hidden inside."],
 "ENVELOPE", "STAMP PARCEL POSTCODE LETTERBOX COUNTER SCALES TELEGRAM PIGEONHOLE POSTMARK AIRMAIL MAILBAG COURIER STATIONERY REGISTERED SORTING"),

("Vigil in the Crypt", "The crypt of St. Alder's Church",
 "Beneath St. Alder's, the crypt is cold and very quiet. The sexton swears someone has been visiting after dark. He leads you down the worn steps, where something has dripped on every stone, and the smell of smoke still hangs in the air. 'Whoever it was,' he murmurs, 'left in a great hurry.'",
 ["Wax drips lead down the steps.", "A small flame left a black smudge on the wall.", "It was lit, then snuffed out in a hurry."],
 "CANDLE", "VAULT TOMB ALTAR CHALICE INCENSE ARCHWAY COBWEB EPITAPH CHAPEL SHADOW TAPESTRY STAIRCASE HYMNBOOK DAMP RELIC"),

("Rain at the Bus Stop", "The bus shelter on Mill Lane",
 "It rained hard on the night of the murder, and Dr. Odette Marsh remembers the bus shelter well. A figure waited there, perfectly dry, though the downpour hammered the roof. The last bus never came. 'They carried something tall and dark,' she says, 'folded tight, and they forgot it on the bench.'",
 ["Black cloth stretched over thin metal spokes.", "A curved handle hangs over the bench.", "Left behind by someone who stayed dry."],
 "UMBRELLA", "PUDDLE RAINCOAT TIMETABLE SHELTER BENCH GUTTER DRIZZLE THUNDER MUDDY WELLIES DRIVER FARE PASSENGER ROUTE COBBLES"),

("Boathouse Lights", "The river boathouse",
 "At the river boathouse, the ferryman reports a light bobbing over the water at midnight, the very hour Ambrose died. 'Too steady for a torch,' he mutters, 'too small for a bonfire.' You find a ring of scorched grass on the jetty, and a warm patch where someone sat and watched the clockmaker's windows.",
 ["A glass shield protects the flame.", "It swings from an iron handle.", "Hung from the bow of a small boat."],
 "LANTERN", "PADDLE JETTY CANOE REEDS MOORING DINGHY LIFEJACKET RUDDER SCULL WILLOW HERON PONTOON LOCK CURRENT RAFT"),

("The Allotment Gate", "The allotments behind Church Row",
 "Wilf Ottley's allotment is the pride of Marrowby, yet this morning his shed door would not budge. Someone fitted a new fastening during the night, and Wilf does not own the key. 'Not mine,' he grumbles, 'and not cheap either.' Between the cabbages you spot a single small footprint pointing towards the village.",
 ["Cold, heavy brass with a curved shackle.", "It hangs from a bolted hasp.", "It needs a small key, which is missing."],
 "PADLOCK", "SPADE COMPOST CABBAGE LEEKS PARSNIP RHUBARB HOSEPIPE SHED CUCUMBER MARROW FURROW SEEDLING WEEDS BEETROOT POTATO"),

("Fete Rosette", "The summer fete on the green",
 "At the summer fete, the Best Victoria Sponge award went to Nell Crumpet for the fifth year running. But part of her prize has gone missing, and the rival bakers are whispering. Someone tampered with the judges' table while the band played, and you notice a smear of icing on the tent pole.",
 ["Silky cloth that curls at both ends.", "Pinned beneath the first-prize rosette.", "Tied around a silver cup in a neat bow."],
 "RIBBON", "BUNTING TOMBOLA COCONUT RAFFLE SPONGE MARQUEE TRESTLE JUDGE PRIZE CUSTARD LEMONADE BANDSTAND HOOPLA FUDGE WINNER"),

("Silence in the Library", "Marrowby Library",
 "Ines Calloway guards the village library like a dragon in a cardigan. This morning she found the reading-room desk disturbed: a blotted page, a ring of stains and a drawer left open. 'Ambrose signed something here,' she says, 'the week before he died. And now the page is torn from my register.'",
 ["A dark ring stains the desk.", "A feather pen lies beside it, still wet.", "A little glass pot, now empty."],
 "INKWELL", "SHELF NOVEL CATALOGUE LIBRARIAN BOOKMARK ARCHIVE ATLAS PAPERBACK REFERENCE BORROW OVERDUE SPINE CHAPTER READER DICTIONARY"),

("Greenhouse Tremors", "Hattie Brightwell's greenhouse",
 "Hattie Brightwell's greenhouse is a jungle of ferns and tomatoes. She noticed fresh soil on the path and muddy prints leading to the door. 'Somebody dug where nothing was planted,' she says, 'right under the old rosebed. They hurried off and left their tool in a flowerpot.'",
 ["A pointed blade on a short wooden handle.", "Used for digging small holes.", "Found muddy in a flowerpot."],
 "TROWEL", "TOMATO GERANIUM FERN WATERCAN TERRACOTTA PETUNIA ORCHID CUTTINGS SEEDTRAY VINE POTTING TRELLIS HUMID BLOSSOM CACTUS"),

("The Piano Recital", "Marrowby Village Hall",
 "The old piano in the village hall was tuned the very week Ambrose died. The tuner says one note sounded dull, as if something were stuck beneath it. When he lifted the lid, he found a tiny folded paper, and a small piece of the keyboard chipped away. 'Someone wanted this hidden,' he says quietly.",
 ["A pale, smooth surface.", "Elephant tusks once provided it.", "It lies beside the black keys."],
 "IVORY", "PIANO STOOL KEYBOARD SONATA PEDAL METRONOME CONCERT AUDIENCE ENCORE MELODY ARPEGGIO TUNER RECITAL APPLAUSE LULLABY"),

("The Stable Door", "The stables at Vance Manor",
 "At Vance Manor, the groom found one stall empty and a leather item missing from its peg. Lady Cordelia insists that nothing was stolen. 'Then why,' says the groom, 'did someone ride out at midnight? The mud on the lane was fresh, and the hoofprints were deep, as if the rider carried a heavy load.'",
 ["Padded leather with a curved seat.", "It sits on a horse's back.", "Two stirrups hang from its sides."],
 "SADDLE", "PONY STIRRUP BRIDLE HAYLOFT MANE HOOF PADDOCK GROOM FARRIER TROUGH REINS STALLION GALLOP OATS BLANKET"),

("Last Train to Marrowby", "Marrowby Halt railway station",
 "Marrowby Halt sees only two trains a day. The stationmaster remembers a man in a hurry on the night of the murder, who paid no fare and gave no name. 'He dropped something,' the old man says, 'and I kept it, in case he came back.' It has been sitting in a drawer ever since.",
 ["A rectangle of stiff card with a punched hole.", "It shows a destination and a date.", "Passengers must show it to the guard."],
 "TICKET", "PLATFORM SIGNAL GUARD CARRIAGE SLEEPER BUFFER TUNNEL STOKER TERMINUS LEVER PORTER LUGGAGE SIDING BRAKE EXPRESS"),

("The Cloakroom Mix-up", "The village hall cloakroom",
 "At the village dance, Major Ashgrove's garment went missing from the cloakroom. It was heavy tweed, long to the knee, with deep pockets and one loose button. 'In the pocket was a key to Ambrose's shop,' the Major confesses, 'and now both are gone.' The attendant swears she never left her post.",
 ["A long, heavy outer garment.", "It has deep pockets and brass buttons.", "Worn over everything else in winter."],
 "OVERCOAT", "HANGER SCARF GLOVES HATSTAND LABEL BONNET MUFFLER BASKET SHAWL CORRIDOR CURTAIN BROLLY LINING POCKET BUTTON"),

("The Midnight Chime", "The tower of St. Alder's",
 "The church bell rang at midnight, though no ringer was on duty. The vicar climbs the tower with you and finds the pull hanging oddly short. Someone has cut it with a sharp blade and carried the missing piece away. Pigeons scatter as you search the dusty floor, where a single boot print points to the stairs.",
 ["Thick braided cord with a woolly grip.", "Cut clean through with a blade.", "It hangs from the tower ceiling to the floor."],
 "BELLROPE", "BELFRY STEEPLE CLAPPER PEAL TOLL CHIME PIGEON LADDER GARGOYLE WEATHERVANE CLOCKFACE RINGER TOWER GALLERY SPIRAL"),

("The Antique Shop", "Fenn's Antiques",
 "Tobias Fenn's antique shop smells of beeswax and old secrets. He is helpful, perhaps too helpful, and offers to show you the paperwork for a clock he sold to Ambrose. 'I keep everything in perfect order,' he smiles. One page, however, is missing from the pile, and his smile slips for just a second.",
 ["Names, dates and prices in a tidy column.", "Sent with the goods, before payment.", "The page with the total is missing."],
 "INVOICE", "VASE PORCELAIN CABINET MAHOGANY CHANDELIER CURIO TRINKET VELVET AUCTION BROOCH PEWTER GRAMOPHONE SNUFFBOX MIRROR CANDELABRA"),

("Baking at Dawn", "Crumpet's Bakery",
 "Nell Crumpet rises at four to bake. This morning she found flour footprints around her ovens and an empty hook by the door. 'Someone borrowed it,' she says, 'and left a thumbprint in the dough.' The only other thing out of place is a jam stain on the windowsill, still sticky.",
 ["A cotton garment tied at the waist.", "Splashed with flour and jam.", "It hangs on a hook by the door."],
 "APRON", "LOAF DOUGH OVEN CRUST BAGUETTE CROISSANT YEAST FLOUR WHISK PASTRY BRIOCHE TART KNEAD GLAZE BATCH"),

("The Scarecrow Field", "Farmer Gilbey's barley field",
 "Farmer Gilbey says the crows have stopped landing in his barley. Last night, someone moved his guardian across the field, dug a hole beneath it, and filled it in again. 'Why would anyone bury anything in my wheat?' he grumbles. You notice a torn scrap of cloth snagged on the fence.",
 ["A straw-stuffed figure on a pole.", "It wears old clothes and a floppy hat.", "It stands in fields to frighten the birds."],
 "SCARECROW", "HARVEST STRAW HAYSTACK TRACTOR BARLEY WHEAT SCYTHE PLOUGH MEADOW FENCE HEDGEROW MAGPIE STILE PASTURE SILO"),

("The Pigeon Loft", "Major Ashgrove's loft",
 "Major Ashgrove keeps racing pigeons, and one came home on the night of the murder with a tiny scroll tied to its leg. In the loft you find the scroll gone and something light and grey caught in the latch. 'My birds are careful,' he says. 'Somebody else was in here.'",
 ["Light as air and edged with grey.", "Found on the floor of the loft.", "Once dipped in ink to write letters."],
 "FEATHER", "COOP ROOSTER BANTAM FEEDER NESTING PERCH PLUMAGE HATCH CLUTCH GOOSE DUCKLING CHICKEN GRAIN TURKEY BEAK"),

("The Painter's Studio", "The old schoolhouse studio",
 "The village artist works in the old schoolhouse. One portrait of Lady Cordelia has been slashed, and the canvas turned to face the wall. 'It stood right there,' he says, pointing at bare floorboards and three round dents in the dust. 'Now it has gone, and so has my best brush.'",
 ["A wooden stand with three legs.", "It holds a canvas upright.", "Splashed with every colour."],
 "EASEL", "PALETTE CANVAS BRUSH PORTRAIT LANDSCAPE SKETCH PIGMENT VARNISH MODEL FRAME STUDIO SMOCK TURPENTINE MURAL SCENERY"),

("The Manor Safe", "Lady Cordelia's study",
 "Lady Cordelia leads you into her late husband's study. The wall safe stands open and a velvet box lies empty. 'Diamonds,' she sighs, 'on a silver chain I wore to every ball.' She does not quite meet your eye, and her tea has gone cold. Ambrose repaired the safe's clockwork only a week ago.",
 ["Worn around the throat.", "A chain strung with sparkling stones.", "Kept in a velvet box, now empty."],
 "NECKLACE", "STUDY DIAMOND PEARL RUBY HEIRLOOM DECANTER FIREPLACE GLOBE TASSEL MANTEL COMBINATION BUTLER SAPPHIRE CHEQUE ESTATE"),

("Market Day", "The Marrowby market square",
 "On market day the square is loud with traders. The spice seller says a customer asked for one small brown seed and paid with old coins. 'Grated over puddings,' she says, 'and a little goes a long way. But he wanted the whole thing, wrapped in a handkerchief.' You spot the handkerchief in the gutter.",
 ["A hard brown seed the size of an olive.", "Grated into puddings and eggnog.", "Warm and sweet in flavour."],
 "NUTMEG", "STALL BARROW CHEESE HONEY PICKLE SAUSAGE TRADER SAFFRON CINNAMON GINGER PEPPER CLOVES BARGAIN HAGGLE AWNING"),

("The Sweet Shop", "Mr Pym's sweet shop",
 "Mr Pym's sweet shop has fed the village for forty years. A jar was emptied overnight, and a note was left behind: 'For Ambrose.' Mr Pym says the missing sweet was Ambrose's favourite, a treat so sticky it once pulled out a filling. 'Why would a thief take only that?' he wonders.",
 ["Chewy, buttery and golden brown.", "It sticks to your teeth.", "Made by boiling sugar with butter."],
 "TOFFEE", "LIQUORICE HUMBUG GOBSTOPPER LOLLIPOP JELLY SHERBET NOUGAT CARAMEL TREACLE WRAPPER SWEETS TRUFFLE BONBON MARSHMALLOW PEPPERMINT"),

("Picnic by the Weir", "The weir meadow",
 "The Sunday school picnic ended with a muddy surprise. The big wicker container was found floating in the weir, empty except for a single envelope. 'We packed sandwiches,' says the curate's wife, 'not secrets.' Footprints at the water's edge show that someone dragged it there from the bandstand.",
 ["A large basket with a lid.", "Packed with sandwiches and cake.", "Carried by two handles to the riverbank."],
 "HAMPER", "WEIR SANDWICH FLASK PICNIC GRASS DAISY BUTTERFLY SUNHAT PASTY CRISPS SALAD STREAM CLOVER DRAGONFLY NAPKIN"),

("Fire Station Open Day", "Marrowby Fire Station",
 "Captain Moss hosts an open day at the village fire station. On the night Ambrose died, the brigade was called to a false alarm at his workshop. By the time they returned, the old fire cart would not start. 'Someone tampered with the part that makes it go,' the captain growls.",
 ["Pistons, cylinders and a rattling heart.", "It burns fuel to make a vehicle move.", "Lift the bonnet to find it."],
 "ENGINE", "HOSE SIREN HELMET HYDRANT BRIGADE RESCUE PUMP BLAZE SMOKE ALARM BADGE SPRINKLER CAPTAIN DRILL SOOT"),

("The Boatyard", "Dunmore's Boatyard on the river",
 "The old sailor swears a small boat slipped its mooring on the night of the murder without a crew. 'It left a deep scar in the mud,' he says. 'Something heavy was dragged ashore, then dropped to hold her fast.' You find a rusty trail along the bank, ending at the water.",
 ["A heavy iron hook with two flukes.", "Dropped over the bow of a ship.", "Holds a vessel still on the river bed."],
 "ANCHOR", "HULL MAST RIGGING KEEL BOSUN DOCKYARD TIMBER PLANK CHANDLER SAILOR CABIN GALLEY ROPE DECK HARBOUR"),

("The Tailor's Fitting Room", "Dunnock & Son, Tailors",
 "At the tailor's, Mr Dunnock measured Ambrose for a new suit the week before his death. He remembers a pin-prick of blood on the lapel and a note: 'Let out the waist.' Now something sharp is missing from the pincushion, and a trail of thread leads to the back door.",
 ["Thin, sharp and made of steel.", "It has an eye at one end.", "Pulled through fabric, trailing thread."],
 "NEEDLE", "THREAD THIMBLE PATTERN CHALK SEAM HEMLINE SUIT BOBBIN ZIPPER TAILOR COLLAR SLEEVE TROUSERS CUFFLINK FITTING"),

("Stargazers' Hill", "The observatory on the hill",
 "The retired schoolmaster keeps a brass instrument at the top of the hill. On the night of the murder, he saw a window glowing in the clockmaker's shop. 'I wasn't looking at the stars,' he admits, 'I was looking at the lamp.' Then he frowns. 'And someone has moved it since.'",
 ["A long brass tube on three legs.", "It brings faraway things close.", "Aimed at the sky from the hill."],
 "TELESCOPE", "COMET PLANET ORBIT GALAXY METEOR DOME ECLIPSE NEBULA STARLIGHT LENS ASTRONOMER SATURN JUPITER ZODIAC MOONBEAM"),

("The Constable's Desk", "Marrowby Police House",
 "Constable Ned Harcourt's desk is neat except for one thing: a small tin has been left open and a purple smear stains the blotter. 'Someone pressed their fingertips here,' he says, 'though they never signed the register.' He rubs his chin. 'Whoever it was had very clean hands.'",
 ["A flat tin with a soft cushion.", "Soaked with purple ink.", "Fingers press into it to leave prints."],
 "INKPAD", "HANDCUFFS TRUNCHEON CELL REPORT WITNESS ALIBI SUSPECT FINGERPRINT STATEMENT PATROL LOCKUP CONSTABLE MOTIVE NOTEPAD DESK"),

("The Quilting Circle", "Mabel's back room",
 "The Thursday sewing circle meets in Mabel's back room. A prized blanket, stitched over twenty years by six pairs of hands, has gone missing, and with it a scrap of Ambrose's old waistcoat sewn in as a keepsake. 'It was warm and heavy,' Mabel sniffs, 'and far too big to carry unseen.'",
 ["Layers of cloth stitched together.", "Warm, padded and patterned.", "Spread across a bed in winter."],
 "QUILT", "PATCHWORK FABRIC STITCH BINDING WADDING COTTON LINEN SQUARE HOOP SCISSORS PINCUSHION CALICO FLANNEL BORDER APPLIQUE"),

("The Strumming Society", "The Reading Room",
 "The Strumming Society meets in the Reading Room. Their tiny star player vanished on the night of the murder. Ambrose loved to listen, and once said that its sound reminded him of sunshine on a faraway island. Under his chair at the last rehearsal, someone found three sheets of music.",
 ["Four strings and a small wooden body.", "Bright and plinky, from Hawaii.", "Smaller than a guitar."],
 "UKULELE", "CHORD STRINGS TUNING REHEARSAL BANJO FIDDLE HARMONY TAMBOURINE ACCORDION CHORUS VERSE RHYTHM SONGBOOK STRUM CHOIR"),

("The Guest House Breakfast", "Mrs Plover's guest house",
 "At Mrs Plover's guest house, a lodger left without paying and without finishing his breakfast. His boiled egg lay rolling across the tablecloth, and its little stand was gone. 'Silly thing to steal,' she says. 'Unless it was hiding something small.' You notice the lodger's room key is also missing.",
 ["A little porcelain cup with a hollow.", "Holds a boiled egg upright.", "Found beside a plate of toast."],
 "EGGCUP", "BACON TOAST PORRIDGE KIPPER MUSHROOM CEREAL YOGHURT LANDLADY GUESTBOOK LODGER BEDROOM PANCAKE MUFFIN BREAKFAST LANDING"),

("The Flower Show", "The Marrowby Flower Show",
 "At the Flower Show, a prize yellow bloom was swapped for a plastic one overnight. Hattie Brightwell is furious. 'They are the first sign of spring,' she says, 'and that was the finest of the whole lot.' Nobody saw the swap, but the tent flap was tied with a clumsy knot.",
 ["A yellow spring bulb.", "Shaped like a trumpet.", "Nods in the breeze every March."],
 "DAFFODIL", "TULIP PEONY LAVENDER POPPY HYACINTH FOXGLOVE BLUEBELL MARIGOLD PRIMROSE BOUQUET PETAL CROCUS DAHLIA JASMINE WISTERIA"),

("The Military Museum", "Major Ashgrove's museum",
 "Major Ashgrove curates the tiny museum above the post office. A mannequin's jacket was disturbed last night, and a golden ornament was taken from the shoulder. 'It shows rank,' he growls. 'Whoever took it wishes to be mistaken for an officer.' He taps the glass. 'Or wants me to think so.'",
 ["A fringed ornament on the shoulder.", "It marks a soldier's rank.", "Gold braid stitched to a jacket."],
 "EPAULETTE", "MEDAL BAYONET REGIMENT BUGLE CANNON MUSKET UNIFORM TRENCH BARRACKS SABRE SERGEANT BANNER CAMPAIGN ARMOUR MAJOR"),

("The Whispering Woods", "Whispering Woods",
 "Constable Harcourt follows boot prints into Whispering Woods, where someone has dug a patch beneath a great tree. A squirrel scolds from above. 'Whoever it was,' he says, 'was looking for something small and brown that falls in autumn.' He brushes the soil, and finds a button with a thread still attached.",
 ["It falls from an oak in autumn.", "A squirrel's favourite snack.", "A small brown nut wearing a little cap."],
 "ACORN", "BRAMBLE BADGER BEECH THICKET TOADSTOOL SQUIRREL MOSS CLEARING TWIG HOLLOW ANTLER PINECONE BIRCH LICHEN FOOTPATH"),

("The Grocer's Accounts", "Pickering's Grocers",
 "Old Mr Pickering the grocer keeps a heavy book of credit and debts. Ambrose owed him nothing, yet his name has been scribbled out and rewritten in a different hand. 'Somebody doctored the figures,' Pickering says. 'The ink is too fresh and the handwriting is too neat for mine.'",
 ["A bound book of accounts.", "Columns for debts and payments.", "Every sale written in neat ink."],
 "LEDGER", "SHOPKEEPER TILL RECEIPT DEBT CREDIT SACK PRICE CRATE GROCER DELIVERY SHILLING TALLY RATIONS BALANCE FARTHING"),

("Jam Day", "The Women's Institute hall",
 "Jam day at the Institute gets heated. Someone has spoiled Nell Crumpet's purple preserve by stirring in salt, and a trail of small, dark, sticky stains leads from the stove to the garden path. 'Those grow wild by the churchyard wall,' Nell says, 'and nobody picks them but me.'",
 ["Tiny dark purple berries.", "They grow in clusters on a hedge shrub.", "Made into wine and syrup against colds."],
 "ELDERBERRY", "PRESERVE STRAWBERRY GOOSEBERRY DAMSON PECTIN APRICOT SIMMER BOTTLING CHUTNEY RASPBERRY CHERRY INSTITUTE SECRETARY TREASURER CHAIRWOMAN"),

("The Cookery Class", "The cookery class at the school",
 "Dr. Marsh joined the village cookery class to unwind. Last Tuesday the teacher found a page ripped from the class folder. Written on it, she swears, were the quantities and method for Ambrose's favourite pie. 'It was in his late mother's handwriting,' she says, 'and I never even copied it.'",
 ["A list of ingredients and steps.", "Tells you how to cook a dish.", "Often passed down in a grandmother's handwriting."],
 "RECIPE", "CASSEROLE SAUCEPAN SPATULA COLANDER GRATER CHOPPING SEASONING STEWPOT MIXER TEASPOON SOUFFLE PUDDING GRAVY PARSLEY SKILLET"),

("The Cricket Pavilion", "Marrowby Cricket Club",
 "The cricket club met on the green the afternoon before the murder. The umpire says a sharp, shrill sound was heard to stop play, but nobody admits to blowing it. A small metal object has vanished from his pocket, and the scorer insists she saw Fergus Dunmore near the pavilion.",
 ["Small, metal and shrill.", "Blown to stop a game.", "Hangs from a cord around the neck."],
 "WHISTLE", "WICKET BOWLER UMPIRE CREASE STUMPS BAILS INNINGS BOUNDARY SCOREBOARD PAVILION LEATHER PADS CATCH MATCH FIELDER"),

("The Clockmaker's Workshop", "Ambrose Wickes's workshop",
 "Ambrose Wickes's workshop is as he left it, ticking faintly. Among the clutter, you find a gap on the shelf where something once stood. Dust shows its outline, narrow in the middle. 'He used it,' says the constable, 'to time his tea, his eggs and his arguments.'",
 ["Two glass bulbs joined at a narrow waist.", "Sand trickles from top to bottom.", "Marks the time when you turn it over."],
 "HOURGLASS", "PENDULUM COGWHEEL SPRING DIAL TICKING WINDING GEARS MINUTE CUCKOO CHRONOMETER WORKBENCH LOUPE ESCAPEMENT BRASS MIDNIGHT"),

("The Windmill", "Marrowby Windmill",
 "At the old windmill, the miller reports squeaks in the night. Every gear is quiet but one, and the miller says a few drops would cure it, yet his own container has vanished, along with a ladder from the loft. Someone has been working up here in the dark, and left a boot print in the flour.",
 ["A small tin with a long, thin spout.", "Squeezed to drip oil on hinges.", "It silences a squeaky gate."],
 "OILCAN", "MILLSTONE SAILS MILLER HOPPER GRINDING COGS GALE CORNMEAL BREEZE MILLPOND TURRET BEAMS SPINDLE LOFT ROTATE"),

("Behind the Church", "The churchyard",
 "Behind the church, among the mossy headstones, the sexton found a tiny gold keepsake half-buried near the grave of Ambrose's wife. It opens like a shell. 'There is a curl of hair inside,' he whispers, 'and a faded picture.' Fresh flowers lie on the grave, yet nobody admits to leaving them.",
 ["A small gold case worn on a chain.", "It opens to hold a photograph.", "Keeps a curl of hair close to the heart."],
 "LOCKET", "HEADSTONE LYCHGATE MAUSOLEUM CROSS INSCRIPTION WREATH RAVEN SEXTON MOURNER ANGEL MEMORIAL VERGER BURIAL CHURCHYARD MIST"),

("The Ice House", "The ice house at Vance Manor",
 "In the grounds of Vance Manor stands the old ice house, a domed brick cave once used to keep winter's chill all year. Someone has been here: scratch marks line the floor and a hole pierces a block of old straw. 'Slow work,' the gardener says. 'You would need something narrow and strong.'",
 ["A long metal spike with a wooden handle.", "Chips a block into fragments.", "Sharp enough to break frozen water."],
 "ICEPICK", "FROZEN SAWDUST CHILL DRIPPING GLACIER FROST SNOWDRIFT UNDERGROUND WINTER LARDER SHIVER BRICKWORK PASSAGE ARCHED FREEZING"),

("The Dance Hall", "The spring dance at the village hall",
 "At the spring dance, Lady Cordelia lost something precious while whirling across the floor. A single sparkle was found beside the buffet. 'It was one of a pair,' she says, 'a gift from my husband, and now only one remains.' She glances at Tobias Fenn, who looks away.",
 ["Worn on the ear.", "It comes in pairs.", "Dangles, glitters, and is easily lost."],
 "EARRING", "WALTZ FOXTROT TANGO POLKA QUICKSTEP BALLROOM PARTNER ORCHESTRA SEQUINS TWIRL SAXOPHONE CHAPERONE GLITTER MASQUERADE DANCEFLOOR"),

("Game Night at the Goose", "The Gilded Goose public house",
 "At the Gilded Goose, landlord Fergus Dunmore runs game night every Friday. One piece was missing from his set, and with it the end of Ambrose's last game. 'Dots on one side, nothing on the other,' says Fergus, 'and it lay face down all evening, until it vanished.'",
 ["A flat tile with dots.", "Played in a line, end to end.", "Knock one over and the rest fall."],
 "DOMINO", "DARTS SKITTLES CRIBBAGE TANKARD LANDLORD COASTER BARMAID INGLENOOK CIDER BITTER DARTBOARD JUKEBOX TAPROOM PINTS SNOOKER"),

("Magic Night", "The Great Alfredo's show",
 "The Great Alfredo performed at the village hall on the night before the murder. He pulled a coin from Ambrose's ear and a dove from his sleeve. But a favourite prop vanished for real, the one that every rabbit knows well. 'I swear I put nothing inside it,' he says, 'but it was heavy.'",
 ["Tall, black and silky.", "A rabbit hops out of it.", "A gentleman's formal headwear."],
 "TOPHAT", "WAND RABBIT ILLUSION VANISH SLEIGHT CONJURER SPELL TRICK MAGICIAN ABRACADABRA PRESTO SPOTLIGHT ASSISTANT MYSTERY COINS"),

("The Costume Room", "The Marrowby Players' theatre",
 "The Marrowby Players keep their costumes in the old theatre. Someone has rummaged through the tallest piece of furniture backstage, leaving a velvet cloak on the floor and the doors wide open. 'They were hiding in there,' says the director, 'and they left in a hurry, taking my best wig.'",
 ["A tall cupboard for hanging clothes.", "Doors on the front, a rail inside.", "A fine hiding place in a play."],
 "WARDROBE", "COSTUME RUFFLE CORSET CROWN MASK BUSTLE TIARA PROPS BACKSTAGE DIRECTOR ACTRESS PROMPTER GREASEPAINT MANNEQUIN CAPE"),

("The Garden Party", "Vance Manor gardens",
 "Lady Cordelia held a garden party the evening before Ambrose's death. Hattie says she found a cream card tucked into a hedge, embossed in gold, with a name crossed out. 'Not everyone who came was meant to be here,' she whispers. The ink on the crossed-out name is still dark.",
 ["A gold-embossed card.", "It says when and where.", "Sent to those who are asked to attend."],
 "INVITATION", "LAWN GAZEBO CROQUET CHAMPAGNE PARASOL CANAPES TERRACE FOUNTAIN HEDGE GUESTS HOSTESS ORCHARD SUMMER ARBOUR PEACOCK"),

("The Wine Cellar", "The cellar of the Gilded Goose",
 "The cellar of the Gilded Goose is cool and dark. Fergus noticed a bottle opened without a sound and left on a barrel, the stopper pulled out neatly. 'Whoever did it came prepared,' he says. 'The tool is missing from the hook, and it is not mine to lend.'",
 ["A spiral of steel with a handle.", "It twists into a cork.", "Used to open a bottle of wine."],
 "CORKSCREW", "BARREL VINTAGE CASK BOTTLE CELLAR VINEYARD GRAPES SOMMELIER BURGUNDY CLARET SHERRY STOPPER RACKING SPARKLING TASTING"),

("The Village Museum", "The Marrowby Museum",
 "In the village museum a glass case has been left unlocked. The curator cannot tell what was stolen, only that something new was added overnight, with a small card. 'It is not in my catalogue,' she says, 'yet it sits in the middle of the display, as if it has always been there.'",
 ["Something shown to the public.", "Behind glass with a small label.", "A lawyer may hold it up in court."],
 "EXHIBIT", "MUSEUM CURATOR DISPLAY ARTEFACT FOSSIL SKELETON POTTERY HISTORY ANCIENT PLAQUE TREASURE DIORAMA GUIDEBOOK SPECIMEN ROMAN"),
]

# ---------- Testi fissi (inglese: e' il libro) ----------
CAST = [
 ("Ambrose Wickes", "The village clockmaker, found dead in his shop at midnight. His watches all stopped at 12:07."),
 ("Reverend Barnaby Quill", "The gentle vicar of St. Alder's. Loves tea, hates gossip, and has a very good memory."),
 ("Dr. Odette Marsh", "The village doctor. Calm, sharp-eyed, and always carrying a small black bag."),
 ("Mabel Pennyfeather", "The postmistress. She knows every letter that passes through Marrowby, and who sent it."),
 ("Major Rupert Ashgrove", "A retired officer who keeps racing pigeons and a tiny museum above the post office."),
 ("Nell Crumpet", "The baker. Her sponge cakes have won the fete five years in a row."),
 ("Fergus Dunmore", "Landlord of the Gilded Goose. Runs the best game night in the county."),
 ("Lady Cordelia Vance", "Mistress of Vance Manor. Elegant, proud, and very good at keeping secrets."),
 ("Wilf Ottley", "The gardener and king of the allotments. Grumbles at everyone, notices everything."),
 ("Ines Calloway", "The librarian. Quiet, precise, and the keeper of every signed register."),
 ("Tobias Fenn", "The antique dealer. Charming and helpful. Perhaps a little too helpful."),
 ("Hattie Brightwell", "The florist. Cheerful, chatty, and fiercely loyal to her flowers."),
 ("Constable Ned Harcourt", "Your friend on the police force. He needs a sharp mind from outside the village. That is you."),
]

PROLOGUE = [
 "Marrowby is the sort of village where everyone knows your business before you do. The cottages lean together, the church clock is always a little slow, and the tea is always strong.",
 "On a stormy night, the clockmaker Ambrose Wickes was found in his workshop. Every clock in the shop had stopped. The door was locked from the inside. Nobody heard a sound.",
 "Constable Harcourt needs help. You have just moved into the cottage by the green, and you are known to be good with puzzles. So he knocks on your door with a lantern in one hand and a notebook in the other.",
 "'Fifty small mysteries,' he says. 'Fifty people with something to hide. Solve them one by one, and the truth about Ambrose will come out.'",
 "Each case has a short story, three clues and a puzzle grid. Solve the grid, find the hidden clue word, and write it in your Evidence Board. Fifty words will tell you who did it.",
]

HOWTO = [
 ("1.", "Read the story on the left-hand page. It contains three clues."),
 ("2.", "Turn to the puzzle on the right-hand page. Find the 15 words on the list. They can run in any direction: across, down, diagonally, and backwards."),
 ("3.", "There is also a 16th word hidden in the grid. It is NOT on the list. It is the clue word of the case."),
 ("4.", "Use the three clues from the story to guess it. When you find it, write it on the line under the grid."),
 ("5.", "Copy it into the Evidence Board at the front of the book."),
 ("6.", "After Case 50, turn to The Final Case. Take the first letter of each clue word, in order, and read the message."),
 ("7.", "Stuck? Full solutions are at the back of the book. No peeking at the very last page until you have your answer!"),
]

FINAL_STORY = [
 "At last you stand in the clockmaker's workshop once more, with Constable Harcourt beside you and fifty clue words in your notebook.",
 "The door was locked from the inside. The clocks had stopped at 12:07. A will had been changed, and a rare collection of clocks had been sold. Somebody in Marrowby knew exactly what Ambrose Wickes owned, and exactly what it was worth.",
 "Everyone in the village is a suspect: the vicar, the doctor, the postmistress, the Major, the baker, the landlord, the lady of the manor, the gardener, the librarian, the antique dealer and the florist.",
 "Look again at your Evidence Board. Each clue word is a piece of the night. Together, they point to one name.",
]

DEDUCTION = [
 "Write the FIRST LETTER of each clue word in the boxes below, in order from Case 1 to Case 50.",
 "Then split the letters into words to read the message.",
]

VERDICT_TEXT = [
 "THE CULPRIT IS TOBIAS FENN, THE ANTIQUE DEALER WHO LIED TWICE.",
 "Tobias forged a new will with Ambrose's own INKWELL, sold the clockmaker's collection through a fake INVOICE, and hid the proof in his LEDGER. When Ambrose found out, Tobias returned that night, using the HOURGLASS to time the lock and the key from the OVERCOAT to enter.",
]
