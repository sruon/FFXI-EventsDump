# 17289772 - Peddlestox

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Western Altepa Desert (ID: 125) |
| Block Size       | 328 bytes                       |
| Total Events     | 7                               |
| References Count | 18                              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [65534](#event-65534) | 0x0001       |      1 |              1 |
| [100](#event-100)     | 0x0002       |     23 |             11 |
| [101](#event-101)     | 0x0019       |    108 |             29 |
| [102](#event-102)     | 0x0085       |     11 |              5 |
| [103](#event-103)     | 0x0090       |     55 |             18 |
| [104](#event-104)     | 0x00C7       |     11 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CF4      |        7412 |
|       1 | 0x1CF7      |        7415 |
|       2 | 0x1CF8      |        7416 |
|       3 | 0x1CF9      |        7417 |
|       4 | 0x1CFC      |        7420 |
|       5 | 0x1CFD      |        7421 |
|       6 | 0x00C8      |         200 |
|       7 | 0x0000      |           0 |
|       8 | 0x00B4      |         180 |
|       9 | 0x1CFE      |        7422 |
|      10 | 0x1CFF      |        7423 |
|      11 | 0x007D      |         125 |
|      12 | 0x005A      |          90 |
|      13 | 0x1D00      |        7424 |
|      14 | 0x025D      |         605 |
|      15 | 0x1D01      |        7425 |
|      16 | 0x1CF3      |        7411 |
|      17 | 0x1D02      |        7426 |

## String References

- **7411**: What'sa matta with ya, [son/missy]? Ya thinkin' about walkin' arounda these here parts witha no map? Ya gotta be crazy!
- **7412**: When I was a young bambina likesa you, I's seen my share of loot. But over the years, I learneda one thing--the sweetest treasure lies outta sight. Thatsa what I'm collectin'.
- **7415**: I hears that if you wants to talk to one of them crazy Anticans livin' 'round here, you gots to use some strange instrument. Now if I could gets my hands on one of them tasty pieces...
- **7416**: Unfortunately, to keeps their secret, thosea guys always breaks the goods up into four pieces.
- **7417**: If you can finds all four, you brings thema back here to yours truly. I'll make it worth your while.
- **7420**: What'sa that you gots there? Hmmm... It looks likea one of those creepy-crawly Anticans' goods.
- **7421**: I needs to check this out to make sure you're not tryin' to pulla fast one.
- **7422**: You did some good work, kid. Now it'sa time for me to keep up my end of the bargain.
- **7423**: Here, lets me marka your map...
- **7424**: I swears on my grandmama's grave that theresa treasure buried somewhere around there.
- **7425**: What!? You goes where I tells ya, and you'll havea no problem findin' the stash. And don't ya forget your $0!
- **7426**: Whaddo I look like here, a charity?

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

### Event 65534

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 100

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 23 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1E F0 FF FF 7F 1D  00 80 23 1D 01 80 23 1D    ........#...#.
0010: 02 80 23 1D 03 80 23 21  00                       ..#...#!.       
```

#### Opcodes

```
  0: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0007 [0x1D] PRINT_EVENT_MESSAGE(message_id=7412*)
    → "When I was a young bambina likesa you, I's seen my share of loot. But over the years, I learneda one thing--the sweetest treasure lies outta sight. Thatsa what I'm collectin'."
  2: 0x000A [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000B [0x1D] PRINT_EVENT_MESSAGE(message_id=7415*)
    → "I hears that if you wants to talk to one of them crazy Anticans livin' 'round here, you gots to use some strange instrument. Now if I could gets my hands on one of them tasty pieces..."
  4: 0x000E [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000F [0x1D] PRINT_EVENT_MESSAGE(message_id=7416*)
    → "Unfortunately, to keeps their secret, thosea guys always breaks the goods up into four pieces."
  6: 0x0012 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0013 [0x1D] PRINT_EVENT_MESSAGE(message_id=7417*)
    → "If you can finds all four, you brings thema back here to yours truly. I'll make it worth your while."
  8: 0x0016 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0017 [0x21] END_EVENT
 10: 0x0018 [0x00] END_REQSTACK()
```

### Event 101

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0019    |
| Data Size    | 108 bytes |
| Instructions | 18        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             20 01 42 1E F0 FF FF            .B....
0020: 7F 1D 04 80 23 1D 05 80  23 45 06 80 F0 FF FF 7F  ....#...#E......
0030: F0 FF FF 7F 66 64 6F 31  07 80 1C 08 80 45 06 80  ....fdo1.....E..
0040: F0 FF FF 7F F0 FF FF 7F  66 64 69 31 07 80 1D 09  ........fdi1....
0050: 80 23 1D 0A 80 23 89 0B  80 8B 0B 80 07 80 04 10  .#...#..........
0060: 05 10 54 72 65 61 73 75  72 65 00 00 00 00 00 00  ..Treasure......
0070: 00 00 1C 0C 80 1D 0D 80  23 03 02 10 0E 80 1D 0F  ........#.......
0080: 80 23 8A 21 00                                    .#.!.           
```

#### Opcodes

```
  0: 0x0019 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x001B [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x001C [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0021 [0x1D] PRINT_EVENT_MESSAGE(message_id=7420*)
    → "What'sa that you gots there? Hmmm... It looks likea one of those creepy-crawly Anticans' goods."
  4: 0x0024 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0025 [0x1D] PRINT_EVENT_MESSAGE(message_id=7421*)
    → "I needs to check this out to make sure you're not tryin' to pulla fast one."
  6: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0029 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x003A [0x1C] WAIT(180* ticks)
  9: 0x003D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x004E [0x1D] PRINT_EVENT_MESSAGE(message_id=7422*)
    → "You did some good work, kid. Now it'sa time for me to keep up my end of the bargain."
 11: 0x0051 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0052 [0x1D] PRINT_EVENT_MESSAGE(message_id=7423*)
    → "Here, lets me marka your map..."
 13: 0x0055 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0056 [0x89] OPEN_MAP(map_id=0x0000800B)
 15: 0x0059 [0x8B] SET_EVENT_MARK: Add/update map marker on map 125* at (Work_Zone[4], Work_Zone[5]), index=0*, name=(no name)
 16: 0x0062 [0x54] WAIT_MAP_SCHEDULER: Wait for scheduler 0x00000000 with entities [Unknown NPC (ID: 1935762802/0x73616572), Unknown NPC (ID: 6648437/0x00657275)]
 17: 0x006F [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0070 [0x00] END_REQSTACK()
     0x0071 [0x00] END_REQSTACK()
     0x0072 [0x1C] WAIT(90* ticks)
     0x0075 [0x1D] PRINT_EVENT_MESSAGE(message_id=7424*)
    → "I swears on my grandmama's grave that theresa treasure buried somewhere around there."
     0x0078 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0079 [0x03] Work_Zone[2] = 605*
     0x007E [0x1D] PRINT_EVENT_MESSAGE(message_id=7425*)
    → "What!? You goes where I tells ya, and you'll havea no problem findin' the stash. And don't ya forget your $0!"
     0x0081 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0082 [0x8A] CLOSE_MAP()
     0x0083 [0x21] END_EVENT
     0x0084 [0x00] END_REQSTACK()
```

### Event 102

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0085   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                1E F0 FF  FF 7F 1D 10 80 23 21 00       ........#!.
```

#### Opcodes

```
  0: 0x0085 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x008A [0x1D] PRINT_EVENT_MESSAGE(message_id=7411*)
    → "What'sa matta with ya, [son/missy]? Ya thinkin' about walkin' arounda these here parts witha no map? Ya gotta be crazy!"
  2: 0x008D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x008E [0x21] END_EVENT
  4: 0x008F [0x00] END_REQSTACK()
```

### Event 103

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0090   |
| Data Size    | 55 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090: 20 01 42 1E F0 FF FF 7F  89 0B 80 8B 0B 80 07 80   .B.............
00A0: 04 10 05 10 54 72 65 61  73 75 72 65 00 00 00 00  ....Treasure....
00B0: 00 00 00 00 1C 0C 80 1D  0D 80 23 03 02 10 0E 80  ..........#.....
00C0: 1D 0F 80 23 8A 21 00                              ...#.!.         
```

#### Opcodes

```
  0: 0x0090 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0092 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0093 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0098 [0x89] OPEN_MAP(map_id=0x0000800B)
  4: 0x009B [0x8B] SET_EVENT_MARK: Add/update map marker on map 125* at (Work_Zone[4], Work_Zone[5]), index=0*, name=(no name)
  5: 0x00A4 [0x54] WAIT_MAP_SCHEDULER: Wait for scheduler 0x00000000 with entities [Unknown NPC (ID: 1935762802/0x73616572), Unknown NPC (ID: 6648437/0x00657275)]
  6: 0x00B1 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00B2 [0x00] END_REQSTACK()
     0x00B3 [0x00] END_REQSTACK()
     0x00B4 [0x1C] WAIT(90* ticks)
     0x00B7 [0x1D] PRINT_EVENT_MESSAGE(message_id=7424*)
    → "I swears on my grandmama's grave that theresa treasure buried somewhere around there."
     0x00BA [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x00BB [0x03] Work_Zone[2] = 605*
     0x00C0 [0x1D] PRINT_EVENT_MESSAGE(message_id=7425*)
    → "What!? You goes where I tells ya, and you'll havea no problem findin' the stash. And don't ya forget your $0!"
     0x00C3 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x00C4 [0x8A] CLOSE_MAP()
     0x00C5 [0x21] END_EVENT
     0x00C6 [0x00] END_REQSTACK()
```

### Event 104

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C7   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                      1E  F0 FF FF 7F 1D 11 80 23         ........#
00D0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x00C7 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00CC [0x1D] PRINT_EVENT_MESSAGE(message_id=7426*)
    → "Whaddo I look like here, a charity?"
  2: 0x00CF [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00D0 [0x21] END_EVENT
  4: 0x00D1 [0x00] END_REQSTACK()
```
