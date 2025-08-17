# 17719611 - Esmallegue

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 200 bytes                     |
| Total Events     | 3                             |
| References Count | 8                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [885](#event-885)     | 0x0001       |     81 |             15 |
| [894](#event-894)     | 0x0052       |     57 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001D      |          29 |
|       1 | 0x3451      |       13393 |
|       2 | 0x3452      |       13394 |
|       3 | 0x3453      |       13395 |
|       4 | 0x3454      |       13396 |
|       5 | 0x3455      |       13397 |
|       6 | 0x3488      |       13448 |
|       7 | 0x3489      |       13449 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 885

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 81 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A 3B 61 0E 01 F0 FF  FF 7F 66 00 80 F8 FF FF   J;a......f.....
0010: 7F F8 FF FF 7F 74 77 61  30 2B 3B 61 0E 01 01 80  .....twa0+;a....
0020: 23 2B 3B 61 0E 01 02 80  23 2B 3B 61 0E 01 03 80  #+;a....#+;a....
0030: 23 2B 3B 61 0E 01 04 80  23 2B 3B 61 0E 01 05 80  #+;a....#+;a....
0040: 23 66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 77 61 31  #f..........twa1
0050: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x4A] Esmallegue (ID: 17719611/0x010E613B) looks at LocalPlayer
  1: 0x000A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "twa0" with entities [EventEntity, EventEntity], work=29*
  2: 0x0019 [0x2B] Esmallegue (ID: 17719611/0x010E613B) [13393*]:
    → "Greetings, adventurer. San d'Oria is grateful for your services. I am Royal Squire Esmallegue."
  3: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0021 [0x2B] Esmallegue (ID: 17719611/0x010E613B) [13394*]:
    → "Grand Knight Depardal has left his post as sentry in the Outlands. For now he has been enlisted as a member of the city's defense force."
  5: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0029 [0x2B] Esmallegue (ID: 17719611/0x010E613B) [13395*]:
    → "As I'm sure you are already aware, San d'Oria's military is divided into two branches, the Royal Knights and the Temple Knights."
  7: 0x0030 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0031 [0x2B] Esmallegue (ID: 17719611/0x010E613B) [13396*]:
    → "In times of peace, we Royal Knights are charged with the defense of the nation, while the Temple Knights are responsible for maintaining the public order. However, in times of war the Temple Knights are given the role of supervising our ranks."
  9: 0x0038 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0039 [0x2B] Esmallegue (ID: 17719611/0x010E613B) [13397*]:
    → "Unfortunately, this is a source of some conflict. Despite being united under one kingdom, there is strong sense of rivalry between the two armies. It has been said that during the Great War there were many areas of contention between us."
 11: 0x0040 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0041 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "twa1" with entities [EventEntity, EventEntity], work=29*
 13: 0x0050 [0x21] END_EVENT
 14: 0x0051 [0x00] END_REQSTACK()
```

### Event 894

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0052   |
| Data Size    | 57 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       4A 3B 61 0E 01 F0  FF FF 7F 66 00 80 F8 FF    J;a......f....
0060: FF 7F F8 FF FF 7F 74 77  61 30 2B 3B 61 0E 01 06  ......twa0+;a...
0070: 80 23 2B 3B 61 0E 01 07  80 23 66 00 80 F8 FF FF  .#+;a....#f.....
0080: 7F F8 FF FF 7F 74 77 61  31 21 00                 .....twa1!.     
```

#### Opcodes

```
  0: 0x0052 [0x4A] Esmallegue (ID: 17719611/0x010E613B) looks at LocalPlayer
  1: 0x005B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "twa0" with entities [EventEntity, EventEntity], work=29*
  2: 0x006A [0x2B] Esmallegue (ID: 17719611/0x010E613B) [13448*]:
    → "You there, adventurer! I wonder have you heard of the so-called "Cavernous Maws"? That is what many are calling the strange stone effigies appearing throughout Vana'diel."
  3: 0x0071 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0072 [0x2B] Esmallegue (ID: 17719611/0x010E613B) [13449*]:
    → "I don't know if it's true or not, but some say that it was the wicked rituals of Orcish mesmerizers on the stones that caused them to assume that wretched form."
  5: 0x0079 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x007A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "twa1" with entities [EventEntity, EventEntity], work=29*
  7: 0x0089 [0x21] END_EVENT
  8: 0x008A [0x00] END_REQSTACK()
```
