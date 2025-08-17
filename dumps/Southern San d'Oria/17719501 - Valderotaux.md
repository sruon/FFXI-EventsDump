# 17719501 - Valderotaux

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 684 bytes                     |
| Total Events     | 19                            |
| References Count | 25                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [58](#event-58)          | 0x0001       |     17 |              7 |
| [70](#event-70)          | 0x0012       |      1 |              1 |
| [75](#event-75)          | 0x0013       |      1 |              1 |
| [64](#event-64)          | 0x0014       |      1 |              1 |
| [54](#event-54)          | 0x0015       |     17 |              7 |
| [53](#event-53)          | 0x0026       |     17 |              7 |
| [55](#event-55)          | 0x0037       |     22 |              8 |
| [57](#event-57)          | 0x004D       |     64 |             12 |
| [59](#event-59)          | 0x008D       |     17 |              7 |
| [56](#event-56)          | 0x009E       |     17 |              7 |
| [65535.1](#event-655351) | 0x00AF       |     16 |              2 |
| [65535.2](#event-655352) | 0x00BF       |     16 |              4 |
| [65535.3](#event-655353) | 0x00CF       |     16 |              2 |
| [65535.4](#event-655354) | 0x00DF       |     32 |              4 |
| [65535.5](#event-655355) | 0x00FF       |     21 |              3 |
| [65535.6](#event-655356) | 0x0114       |     53 |              5 |
| [888](#event-888)        | 0x0149       |      1 |              1 |
| [889](#event-889)        | 0x014A       |    161 |             39 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0008      |           8 |
|       1 | 0x2361      |        9057 |
|       2 | 0x23A4      |        9124 |
|       3 | 0x23A5      |        9125 |
|       4 | 0x0445      |        1093 |
|       5 | 0x23A6      |        9126 |
|       6 | 0x23A7      |        9127 |
|       7 | 0x001E      |          30 |
|       8 | 0x23A8      |        9128 |
|       9 | 0x23A9      |        9129 |
|      10 | 0x23AA      |        9130 |
|      11 | 0x0078      |         120 |
|      12 | 0x00C8      |         200 |
|      13 | 0x0000      |           0 |
|      14 | 0x0082      |         130 |
|      15 | 0x00C9      |         201 |
|      16 | 0x3487      |       13447 |
|      17 | 0x0001      |           1 |
|      18 | 0x2ECA      |       11978 |
|      19 | 0x0002      |           2 |
|      20 | 0x2EF2      |       12018 |
|      21 | 0x2EF3      |       12019 |
|      22 | 0x2EF4      |       12020 |
|      23 | 0x2F01      |       12033 |
|      24 | 0x2F02      |       12034 |

## String References

- **9057**: Welcome to the Lion Springs! Enjoy our selection of fine food and beverages.
- **9124**: Adventurers must know when opportunity knocks! Though there is a fine line between bravery and foolishness!
- **9125**: I love a good ghost story. The best part about running a tavern is listening to all the tales that adventurers bring from afar.
- **9126**: In Fei'Yin there is an old fountain run dry. They say that you can call a spirit of the dead by simply casting $0 into it. At any rate, that place is a decrepit ruin, so there's no end to the hogwash rumors.
- **9127**: So, the rumor was true? Huzzah! No, I need no thanks. I am happy to just hear your tale.
- **9128**: But what could he mean by a "small dark tight place"? You'd best ask the other patrons or members of your own party for their insight.
- **9129**: Yes, perhaps his corpse was interred in the Garlaige Citadel. What a cruel thing to do!
- **9130**: All's well that ends well, as they say. I've had a ball hearing all about it! Please, stop by if you're ever in the neighborhood.
- **11978**: Ask if this person is the chick's owner? [Yes./No.]
- **12018**: Eh? You have my chocobo, do you?
- **12019**: Well done! He must have been difficult to please when it comes to feeding. Sorry about that. That little bird just loves Lion Springs' cooking.
- **12020**: You are raising a chocobo too, am I correct? Let me teach you a story I often tell my chocobo...
- **12033**: Eh? You say you have my chocobo?
- **12034**: That little bird loves the cooking here. He would never leave this place, not for anything. You must be mistaken.
- **13447**: Your dancing style was...quite unique...

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

### Event 58

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 17 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    38 00 80 1E F0 FF FF  7F 1D 01 80 23 1A 58 01   8..........#.X.
0010: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x38] SET_CLIENT_EVENT_MODE(mode=8*)
  1: 0x0004 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0009 [0x1D] PRINT_EVENT_MESSAGE(message_id=9057*)
    → "Welcome to the Lion Springs! Enjoy our selection of fine food and beverages."
  3: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000D [0x1A] CALL_SUBROUTINE(address=0x0158)
  5: 0x0010 [0x21] END_EVENT
  6: 0x0011 [0x00] END_REQSTACK()
```

### Event 70

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0012  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       00                                            .             
```

#### Opcodes

```
  0: 0x0012 [0x00] END_REQSTACK()
```

### Event 75

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0013  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          00                                          .            
```

#### Opcodes

```
  0: 0x0013 [0x00] END_REQSTACK()
```

### Event 64

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0014  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             00                                        .           
```

#### Opcodes

```
  0: 0x0014 [0x00] END_REQSTACK()
```

### Event 54

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0015   |
| Data Size    | 17 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                38 00 80  1E F0 FF FF 7F 1D 02 80       8..........
0020: 23 1A 58 01 21 00                                 #.X.!.          
```

#### Opcodes

```
  0: 0x0015 [0x38] SET_CLIENT_EVENT_MODE(mode=8*)
  1: 0x0018 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x001D [0x1D] PRINT_EVENT_MESSAGE(message_id=9124*)
    → "Adventurers must know when opportunity knocks! Though there is a fine line between bravery and foolishness!"
  3: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0021 [0x1A] CALL_SUBROUTINE(address=0x0158)
  5: 0x0024 [0x21] END_EVENT
  6: 0x0025 [0x00] END_REQSTACK()
```

### Event 53

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 17 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   38 00  80 1E F0 FF FF 7F 1D 03        8.........
0030: 80 23 1A 58 01 21 00                              .#.X.!.         
```

#### Opcodes

```
  0: 0x0026 [0x38] SET_CLIENT_EVENT_MODE(mode=8*)
  1: 0x0029 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x002E [0x1D] PRINT_EVENT_MESSAGE(message_id=9125*)
    → "I love a good ghost story. The best part about running a tavern is listening to all the tales that adventurers bring from afar."
  3: 0x0031 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0032 [0x1A] CALL_SUBROUTINE(address=0x0158)
  5: 0x0035 [0x21] END_EVENT
  6: 0x0036 [0x00] END_REQSTACK()
```

### Event 55

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 22 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      38  00 80 1E F0 FF FF 7F 03         8........
0040: 02 10 04 80 1D 05 80 23  1A 58 01 21 00           .......#.X.!.   
```

#### Opcodes

```
  0: 0x0037 [0x38] SET_CLIENT_EVENT_MODE(mode=8*)
  1: 0x003A [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x003F [0x03] Work_Zone[2] = 1093*
  3: 0x0044 [0x1D] PRINT_EVENT_MESSAGE(message_id=9126*)
    → "In Fei'Yin there is an old fountain run dry. They say that you can call a spirit of the dead by simply casting $0 into it. At any rate, that place is a decrepit ruin, so there's no end to the hogwash rumors."
  4: 0x0047 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0048 [0x1A] CALL_SUBROUTINE(address=0x0158)
  6: 0x004B [0x21] END_EVENT
  7: 0x004C [0x00] END_REQSTACK()
```

### Event 57

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 64 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         38 00 80               8..
0050: 1E F0 FF FF 7F 1D 06 80  23 5B 07 80 F8 FF FF 7F  ........#[......
0060: F8 FF FF 7F 74 68 6B 31  1D 08 80 23 5B 07 80 F8  ....thk1...#[...
0070: FF FF 7F F8 FF FF 7F 74  68 6B 32 53 F8 FF FF 7F  .......thk2S....
0080: F8 FF FF 7F 74 68 6B 32  1A 58 01 21 00           ....thk2.X.!.   
```

#### Opcodes

```
  0: 0x004D [0x38] SET_CLIENT_EVENT_MODE(mode=8*)
  1: 0x0050 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0055 [0x1D] PRINT_EVENT_MESSAGE(message_id=9127*)
    → "So, the rumor was true? Huzzah! No, I need no thanks. I am happy to just hear your tale."
  3: 0x0058 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0059 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=30*
  5: 0x0068 [0x1D] PRINT_EVENT_MESSAGE(message_id=9128*)
    → "But what could he mean by a "small dark tight place"? You'd best ask the other patrons or members of your own party for their insight."
  6: 0x006B [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x006C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=30*
  8: 0x007B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  9: 0x0088 [0x1A] CALL_SUBROUTINE(address=0x0158)
 10: 0x008B [0x21] END_EVENT
 11: 0x008C [0x00] END_REQSTACK()
```

### Event 59

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008D   |
| Data Size    | 17 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                         38 00 80               8..
0090: 1E F0 FF FF 7F 1D 09 80  23 1A 58 01 21 00        ........#.X.!.  
```

#### Opcodes

```
  0: 0x008D [0x38] SET_CLIENT_EVENT_MODE(mode=8*)
  1: 0x0090 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0095 [0x1D] PRINT_EVENT_MESSAGE(message_id=9129*)
    → "Yes, perhaps his corpse was interred in the Garlaige Citadel. What a cruel thing to do!"
  3: 0x0098 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0099 [0x1A] CALL_SUBROUTINE(address=0x0158)
  5: 0x009C [0x21] END_EVENT
  6: 0x009D [0x00] END_REQSTACK()
```

### Event 56

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009E   |
| Data Size    | 17 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                            38 00                8.
00A0: 80 1E F0 FF FF 7F 1D 0A  80 23 1A 58 01 21 00     .........#.X.!. 
```

#### Opcodes

```
  0: 0x009E [0x38] SET_CLIENT_EVENT_MODE(mode=8*)
  1: 0x00A1 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x00A6 [0x1D] PRINT_EVENT_MESSAGE(message_id=9130*)
    → "All's well that ends well, as they say. I've had a ball hearing all about it! Please, stop by if you're ever in the neighborhood."
  3: 0x00A9 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x00AA [0x1A] CALL_SUBROUTINE(address=0x0158)
  5: 0x00AD [0x21] END_EVENT
  6: 0x00AE [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AF   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                               5B                 [
00B0: 07 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 00     ..........tlk0. 
```

#### Opcodes

```
  0: 0x00AF [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  1: 0x00BE [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BF   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                               1C                 .
00C0: 07 80 6B 69 64 6C 30 F8  FF FF 7F 1C 07 80 00     ..kidl0........ 
```

#### Opcodes

```
  0: 0x00BF [0x1C] WAIT(30* ticks)
  1: 0x00C2 [0x6B] STOP_AND_IDLE: EventEntity stops current action and resets to idle (animation="idl0")
  2: 0x00CB [0x1C] WAIT(30* ticks)
  3: 0x00CE [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CF   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                               5B                 [
00D0: 07 80 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 31 00     ..........thk1. 
```

#### Opcodes

```
  0: 0x00CF [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=30*
  1: 0x00DE [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DF   |
| Data Size    | 32 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                               1C                 .
00E0: 07 80 66 07 80 F8 FF FF  7F F8 FF FF 7F 74 68 6B  ..f..........thk
00F0: 32 53 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 32 00     2S........thk2. 
```

#### Opcodes

```
  0: 0x00DF [0x1C] WAIT(30* ticks)
  1: 0x00E2 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=30*
  2: 0x00F1 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  3: 0x00FE [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FF   |
| Data Size    | 21 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                               1C                 .
0100: 0B 80 45 0C 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..E..........fdo
0110: 31 0D 80 00                                       1...            
```

#### Opcodes

```
  0: 0x00FF [0x1C] WAIT(120* ticks)
  1: 0x0102 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  2: 0x0113 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0114   |
| Data Size    | 53 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:             45 0E 80 F0  FF FF 7F F0 FF FF 7F 63      E..........c
0120: 6D 30 35 0D 80 1C 0B 80  45 0F 80 F0 FF FF 7F F0  m05.....E.......
0130: FF FF 7F 77 68 6F 31 0D  80 55 0F 80 F0 FF FF 7F  ...who1..U......
0140: F0 FF FF 7F 77 68 6F 31  00                       ....who1.       
```

#### Opcodes

```
  0: 0x0114 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm05" with entities [LocalPlayer, LocalPlayer], work=[130*, 0*]
  1: 0x0125 [0x1C] WAIT(120* ticks)
  2: 0x0128 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  3: 0x0139 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=201*
  4: 0x0148 [0x00] END_REQSTACK()
```

### Event 888

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0149  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                             00                             .      
```

#### Opcodes

```
  0: 0x0149 [0x00] END_REQSTACK()
```

### Event 889

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x014A    |
| Data Size    | 161 bytes |
| Instructions | 6         |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                1E F0 FF FF 7F 1C            ......
0150: 07 80 1D 10 80 23 21 00  03 01 10 11 80 43 00 43  .....#!......C.C
0160: 01 02 03 10 0D 80 00 71  01 03 01 10 0D 80 01 EA  .......q........
0170: 01 42 24 12 80 11 80 0D  80 25 02 00 10 0D 80 00  .B$......%......
0180: DA 01 03 01 10 13 80 43  00 43 01 02 03 10 11 80  .......C.C......
0190: 00 C0 01 1D 14 80 23 5B  07 80 F8 FF FF 7F F8 FF  ......#[........
01A0: FF 7F 74 6C 6B 30 1D 15  80 23 5B 07 80 F8 FF FF  ..tlk0...#[.....
01B0: 7F F8 FF FF 7F 74 6C 6B  31 1D 16 80 23 01 D7 01  .....tlk1...#...
01C0: 1D 17 80 23 5B 07 80 F8  FF FF 7F F8 FF FF 7F 74  ...#[..........t
01D0: 6C 6B 30 1D 18 80 23 01  EA 01 02 00 10 11 80 00  lk0...#.........
01E0: EA 01 03 01 10 0D 80 01  EA 01 1B                 ...........     
```

#### Opcodes

```
  0: 0x014A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x014F [0x1C] WAIT(30* ticks)
  2: 0x0152 [0x1D] PRINT_EVENT_MESSAGE(message_id=13447*)
    → "Your dancing style was...quite unique..."
  3: 0x0155 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0156 [0x21] END_EVENT
  5: 0x0157 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0158 [0x03] Work_Zone[1] = 1*
     0x015D [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x015F [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x0161 [0x02] IF !(Work_Zone[3] == 0*) GOTO 0x0171
     0x0169 [0x03] Work_Zone[1] = 0*
     0x016E [0x01] GOTO 0x01EA
     0x0171 [0x42] SET_CLI_EVENT_CANCEL_DATA()
     0x0172 [0x24] CREATE_DIALOG(message_id=11978*, default_option=1*, option_flags=0*)
    → "Ask if this person is the chick's owner? [Yes./No.]"
     0x0179 [0x25] WAIT_DIALOG_SELECT()
     0x017A [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01DA
     0x0182 [0x03] Work_Zone[1] = 2*
     0x0187 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x0189 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x018B [0x02] IF !(Work_Zone[3] == 1*) GOTO 0x01C0
     0x0193 [0x1D] PRINT_EVENT_MESSAGE(message_id=12018*)
    → "Eh? You have my chocobo, do you?"
     0x0196 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0197 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
     0x01A6 [0x1D] PRINT_EVENT_MESSAGE(message_id=12019*)
    → "Well done! He must have been difficult to please when it comes to feeding. Sorry about that. That little bird just loves Lion Springs' cooking."
     0x01A9 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x01AA [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=30*
     0x01B9 [0x1D] PRINT_EVENT_MESSAGE(message_id=12020*)
    → "You are raising a chocobo too, am I correct? Let me teach you a story I often tell my chocobo..."
     0x01BC [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x01BD [0x01] GOTO 0x01D7
     0x01C0 [0x1D] PRINT_EVENT_MESSAGE(message_id=12033*)
    → "Eh? You say you have my chocobo?"
     0x01C3 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x01C4 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
     0x01D3 [0x1D] PRINT_EVENT_MESSAGE(message_id=12034*)
    → "That little bird loves the cooking here. He would never leave this place, not for anything. You must be mistaken."
     0x01D6 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x01D7 [0x01] GOTO 0x01EA
     0x01DA [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01EA
     0x01E2 [0x03] Work_Zone[1] = 0*
     0x01E7 [0x01] GOTO 0x01EA
     0x01EA [0x1B] RETURN
```
