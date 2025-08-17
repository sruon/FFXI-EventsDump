# 17494773 - Heptachiond

## Common Data

| Field            | Value                                |
|------------------|--------------------------------------|
| Zone             | The Eldieme Necropolis [S] (ID: 175) |
| Block Size       | 336 bytes                            |
| Total Events     | 6                                    |
| References Count | 17                                   |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [104](#event-104)     | 0x0001       |     15 |              7 |
| [105](#event-105)     | 0x0010       |     58 |             16 |
| [106](#event-106)     | 0x004A       |     15 |              7 |
| [107](#event-107)     | 0x0059       |    131 |             27 |
| [108](#event-108)     | 0x00DC       |      6 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1F18      |        7960 |
|       1 | 0x1F19      |        7961 |
|       2 | 0x0014      |          20 |
|       3 | 0x1F1A      |        7962 |
|       4 | 0x1F1B      |        7963 |
|       5 | 0x1F1C      |        7964 |
|       6 | 0x03CA      |         970 |
|       7 | 0x1F1D      |        7965 |
|       8 | 0x1F1E      |        7966 |
|       9 | 0x1F1F      |        7967 |
|      10 | 0x1F20      |        7968 |
|      11 | 0x1F21      |        7969 |
|      12 | 0x1F22      |        7970 |
|      13 | 0x1F23      |        7971 |
|      14 | 0x00C9      |         201 |
|      15 | 0x0000      |           0 |
|      16 | 0x1F24      |        7972 |

## String References

- **7960**: I am Heptachiond, a friar from the San d'Orian Cathedral. I am here to pray for the departed.
- **7961**: Many devout believers of the Goddess have been laid to rest here. Sadly, though, the raging war has left their graves desecrated and in ruin.
- **7962**: There is naught I can do for these poor souls, save to light incense as an offering to their memory, and pray for their undisturbed, eternal rest. But alas, I have almost run out of incense.
- **7963**: A friend used to bring me incense, but I have been unable to contact him since he was posted to Fort Karugo-Narugo.
- **7964**: This special incense is handmade by my friend himself, and is imbued with his prayers for the departed. If only I could find a way to acquire more of them...
- **7965**: Oh? Could that possibly be $6 you have in your possession?
- **7966**: Then you have been to Fort Karugo-Narugo and met my friend. It was he who used to offer prayers here.
- **7967**: Even though my friend does not share the same faith as the San d'Orians interred here, he would come here to pray for them all the same. He is truly an admirable person, a model to us all.
- **7968**: But after the outbreak of the war, it became increasingly difficult for him to travel here as in the past. Under these circumstances, I felt it my duty to offer the incense on his behalf.
- **7969**: If some misfortune were to befall me, there would be no one left to honor the memory of the departed.
- **7970**: This graveyard must not be allowed to turn into a sorrowful place haunted by anguished souls.
- **7971**: I will see to it that these faithful children of Altana have the peace they deserve. This is my gift to you. Please accept it.
- **7972**: War is a terrible thing that robs both the living and departed of their peace.

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

### Event 104

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 15 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 1D 01 80 23 21 00   ........#...#!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=7960*)
    → "I am Heptachiond, a friar from the San d'Orian Cathedral. I am here to pray for the departed."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=7961*)
    → "Many devout believers of the Goddess have been laid to rest here. Sadly, though, the raging war has left their graves desecrated and in ruin."
  4: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000E [0x21] END_EVENT
  6: 0x000F [0x00] END_REQSTACK()
```

### Event 105

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 58 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 42 1E F0 FF FF 7F 1D 00  80 23 1D 01 80 23 5B 02  B........#...#[.
0020: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 1D 03 80  .........tlk0...
0030: 23 1D 04 80 23 5B 02 80  F8 FF FF 7F F8 FF FF 7F  #...#[..........
0040: 74 6C 6B 31 1D 05 80 23  21 00                    tlk1...#!.      
```

#### Opcodes

```
  0: 0x0010 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0011 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0016 [0x1D] PRINT_EVENT_MESSAGE(message_id=7960*)
    → "I am Heptachiond, a friar from the San d'Orian Cathedral. I am here to pray for the departed."
  3: 0x0019 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x001A [0x1D] PRINT_EVENT_MESSAGE(message_id=7961*)
    → "Many devout believers of the Goddess have been laid to rest here. Sadly, though, the raging war has left their graves desecrated and in ruin."
  5: 0x001D [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  7: 0x002D [0x1D] PRINT_EVENT_MESSAGE(message_id=7962*)
    → "There is naught I can do for these poor souls, save to light incense as an offering to their memory, and pray for their undisturbed, eternal rest. But alas, I have almost run out of incense."
  8: 0x0030 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0031 [0x1D] PRINT_EVENT_MESSAGE(message_id=7963*)
    → "A friend used to bring me incense, but I have been unable to contact him since he was posted to Fort Karugo-Narugo."
 10: 0x0034 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0035 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
 12: 0x0044 [0x1D] PRINT_EVENT_MESSAGE(message_id=7964*)
    → "This special incense is handmade by my friend himself, and is imbued with his prayers for the departed. If only I could find a way to acquire more of them..."
 13: 0x0047 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0048 [0x21] END_EVENT
 15: 0x0049 [0x00] END_REQSTACK()
```

### Event 106

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 15 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                1E F0 FF FF 7F 1D            ......
0050: 04 80 23 1D 05 80 23 21  00                       ..#...#!.       
```

#### Opcodes

```
  0: 0x004A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x004F [0x1D] PRINT_EVENT_MESSAGE(message_id=7963*)
    → "A friend used to bring me incense, but I have been unable to contact him since he was posted to Fort Karugo-Narugo."
  2: 0x0052 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0053 [0x1D] PRINT_EVENT_MESSAGE(message_id=7964*)
    → "This special incense is handmade by my friend himself, and is imbued with his prayers for the departed. If only I could find a way to acquire more of them..."
  4: 0x0056 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0057 [0x21] END_EVENT
  6: 0x0058 [0x00] END_REQSTACK()
```

### Event 107

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0059    |
| Data Size    | 131 bytes |
| Instructions | 27        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                             42 1E F0 FF FF 7F 03           B......
0060: 02 10 06 80 1D 07 80 23  6F 70 5B 02 80 F8 FF FF  .......#op[.....
0070: 7F F8 FF FF 7F 74 6C 6B  30 1D 08 80 23 1D 09 80  .....tlk0...#...
0080: 23 5B 02 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 31  #[..........tlk1
0090: 1D 0A 80 23 1D 0B 80 23  1D 0C 80 23 53 F8 FF FF  ...#...#...#S...
00A0: 7F F8 FF FF 7F 74 6C 6B  31 5B 02 80 F8 FF FF 7F  .....tlk1[......
00B0: F8 FF FF 7F 70 61 73 30  1D 0D 80 23 53 F8 FF FF  ....pas0...#S...
00C0: 7F F8 FF FF 7F 70 61 73  30 45 0E 80 F8 FF FF 7F  .....pas0E......
00D0: F8 FF FF 7F 71 73 74 63  0F 80 21 00              ....qstc..!.    
```

#### Opcodes

```
  0: 0x0059 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x005A [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x005F [0x03] Work_Zone[2] = 970*
  3: 0x0064 [0x1D] PRINT_EVENT_MESSAGE(message_id=7965*)
    → "Oh? Could that possibly be $6 you have in your possession?"
  4: 0x0067 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0068 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0069 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x006A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  8: 0x0079 [0x1D] PRINT_EVENT_MESSAGE(message_id=7966*)
    → "Then you have been to Fort Karugo-Narugo and met my friend. It was he who used to offer prayers here."
  9: 0x007C [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x007D [0x1D] PRINT_EVENT_MESSAGE(message_id=7967*)
    → "Even though my friend does not share the same faith as the San d'Orians interred here, he would come here to pray for them all the same. He is truly an admirable person, a model to us all."
 11: 0x0080 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0081 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
 13: 0x0090 [0x1D] PRINT_EVENT_MESSAGE(message_id=7968*)
    → "But after the outbreak of the war, it became increasingly difficult for him to travel here as in the past. Under these circumstances, I felt it my duty to offer the incense on his behalf."
 14: 0x0093 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0094 [0x1D] PRINT_EVENT_MESSAGE(message_id=7969*)
    → "If some misfortune were to befall me, there would be no one left to honor the memory of the departed."
 16: 0x0097 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x0098 [0x1D] PRINT_EVENT_MESSAGE(message_id=7970*)
    → "This graveyard must not be allowed to turn into a sorrowful place haunted by anguished souls."
 18: 0x009B [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x009C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
 20: 0x00A9 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=20*
 21: 0x00B8 [0x1D] PRINT_EVENT_MESSAGE(message_id=7971*)
    → "I will see to it that these faithful children of Altana have the peace they deserve. This is my gift to you. Please accept it."
 22: 0x00BB [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x00BC [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
 24: 0x00C9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [EventEntity, EventEntity], work=[201*, 0*]
 25: 0x00DA [0x21] END_EVENT
 26: 0x00DB [0x00] END_REQSTACK()
```

### Event 108

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00DC  |
| Data Size    | 6 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                      1D 10 80 23              ...#
00E0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x00DC [0x1D] PRINT_EVENT_MESSAGE(message_id=7972*)
    → "War is a terrible thing that robs both the living and departed of their peace."
  1: 0x00DF [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00E0 [0x21] END_EVENT
  3: 0x00E1 [0x00] END_REQSTACK()
```
