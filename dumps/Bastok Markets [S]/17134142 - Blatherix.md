# 17134142 - Blatherix

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Bastok Markets [S] (ID: 87) |
| Block Size       | 584 bytes                   |
| Total Events     | 15                          |
| References Count | 28                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [29](#event-29)          | 0x0001       |     18 |              6 |
| [21](#event-21)          | 0x0013       |      1 |              1 |
| [22](#event-22)          | 0x0014       |     43 |              9 |
| [23](#event-23)          | 0x003F       |      1 |              1 |
| [24](#event-24)          | 0x0040       |     38 |              8 |
| [25](#event-25)          | 0x0066       |     57 |             13 |
| [26](#event-26)          | 0x009F       |     43 |              9 |
| [37](#event-37)          | 0x00CA       |     33 |              9 |
| [38](#event-38)          | 0x00EB       |     14 |              6 |
| [188](#event-188)        | 0x00F9       |     29 |              9 |
| [189](#event-189)        | 0x0116       |     14 |              6 |
| [185](#event-185)        | 0x0124       |     89 |             17 |
| [183](#event-183)        | 0x017D       |      1 |              1 |
| [65535.1](#event-655351) | 0x017E       |     11 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x3115      |       12565 |
|       2 | 0x00D7      |         215 |
|       3 | 0x1388      |        5000 |
|       4 | 0x118F      |        4495 |
|       5 | 0x3118      |       12568 |
|       6 | 0x03C1      |         961 |
|       7 | 0x311C      |       12572 |
|       8 | 0x311D      |       12573 |
|       9 | 0x03E8      |        1000 |
|      10 | 0x311E      |       12574 |
|      11 | 0x31C9      |       12745 |
|      12 | 0x31CA      |       12746 |
|      13 | 0x31CB      |       12747 |
|      14 | 0x09EE      |        2542 |
|      15 | 0x11BF      |        4543 |
|      16 | 0x04D9      |        1241 |
|      17 | 0x3382      |       13186 |
|      18 | 0x3383      |       13187 |
|      19 | 0x3386      |       13190 |
|      20 | 0x3387      |       13191 |
|      21 | 0x3388      |       13192 |
|      22 | 0x3389      |       13193 |
|      23 | 0x00C9      |         201 |
|      24 | 0x0000      |           0 |
|      25 | 0xFFFB36C0  |  4294653632 |
|      26 | 0xFFFF55E4  |  4294923748 |
|      27 | 0xFFFFD120  |  4294955296 |

## String References

- **12745**: Ain't you the assistant detective working with the Mythril Musketeers?
- **12746**: They're important customers of mine. Which means, now so are you...and I like to keep my customers happy.
- **12747**: I got all sortsa junk and gossip to trade. Keep me in mind next time you're in town.
- **13186**: You bring me $0, $1, and $2, and I'll cook you up a dose of Goblin Dust. Get it? Got it? Good!
- **13187**: Headin' to the Mythril Musketeers' headquarters soon? Driftlix, or Limpears, as he's known in our circle, is ready when you are.
- **13190**: Oh, it's you. What's that? You wanna thank Limpears?
- **13191**: Sorry, but you just missed him. He left here just a minute ago, skippin' along and whistlin' an old Gobbie tune. I haven't seen him so cheerful since his boss died and the business went under.
- **13192**: It's all thanks to the stable flow of work he's found with the Mythril Musketeers. Now that his future's secured, he can focus on the more important stuff in life, like family.
- **13193**: Seein' him happy puts a smile on my face. I know you can't see it, but I guarantee it's there. Anyway, here's a little somethin' for you, so you can share in on our delight.

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

### Event 29

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 2B 3E 72 05 01 01 80   ........+>r....
0010: 23 21 00                                          #!.             
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(30* ticks)
  2: 0x0009 [0x2B] Blatherix (ID: 17134142/0x0105723E) [12565*]:
    → "I'm a trader. You got anythin' to trade?"
  3: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0011 [0x21] END_EVENT
  5: 0x0012 [0x00] END_REQSTACK()
```

### Event 21

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

### Event 22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 43 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             1E F0 FF FF  7F 1C 00 80 5B 02 80 3E      ........[..>
0020: 72 05 01 3E 72 05 01 74  6C 6B 30 03 02 10 03 80  r..>r..tlk0.....
0030: 03 03 10 04 80 2B 3E 72  05 01 05 80 23 21 00     .....+>r....#!. 
```

#### Opcodes

```
  0: 0x0014 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0019 [0x1C] WAIT(30* ticks)
  2: 0x001C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Blatherix (ID: 17134142/0x0105723E), Blatherix (ID: 17134142/0x0105723E)], work=215*
  3: 0x002B [0x03] Work_Zone[2] = 5000*
  4: 0x0030 [0x03] Work_Zone[3] = 4495*
  5: 0x0035 [0x2B] Blatherix (ID: 17134142/0x0105723E) [12568*]:
    → "A Quadav mine in the Pashhow Marshlands? Bring me 30 $1 or $0 gil, and you bought yourself the information you want."
  6: 0x003C [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x003D [0x21] END_EVENT
  8: 0x003E [0x00] END_REQSTACK()
```

### Event 23

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               00                 .
```

#### Opcodes

```
  0: 0x003F [0x00] END_REQSTACK()
```

### Event 24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0040   |
| Data Size    | 38 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040: 1E F0 FF FF 7F 1C 00 80  5B 02 80 3E 72 05 01 3E  ........[..>r..>
0050: 72 05 01 74 6C 6B 30 03  02 10 06 80 2B 3E 72 05  r..tlk0.....+>r.
0060: 01 07 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x0040 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0045 [0x1C] WAIT(30* ticks)
  2: 0x0048 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Blatherix (ID: 17134142/0x0105723E), Blatherix (ID: 17134142/0x0105723E)], work=215*
  3: 0x0057 [0x03] Work_Zone[2] = 961*
  4: 0x005C [0x2B] Blatherix (ID: 17134142/0x0105723E) [12572*]:
    → "There's an entrance to a mine shaft in the Pashhow Marshlands. You'll need $6 to open the door."
  5: 0x0063 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0064 [0x21] END_EVENT
  7: 0x0065 [0x00] END_REQSTACK()
```

### Event 25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0066   |
| Data Size    | 57 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   42 1E  F0 FF FF 7F 1C 00 80 03        B.........
0070: 02 10 06 80 2B 3E 72 05  01 08 80 23 5B 02 80 3E  ....+>r....#[..>
0080: 72 05 01 3E 72 05 01 74  6C 6B 30 03 02 10 09 80  r..>r..tlk0.....
0090: 03 03 10 04 80 2B 3E 72  05 01 0A 80 23 21 00     .....+>r....#!. 
```

#### Opcodes

```
  0: 0x0066 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0067 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x006C [0x1C] WAIT(30* ticks)
  3: 0x006F [0x03] Work_Zone[2] = 961*
  4: 0x0074 [0x2B] Blatherix (ID: 17134142/0x0105723E) [12573*]:
    → "You need another $3?"
  5: 0x007B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x007C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Blatherix (ID: 17134142/0x0105723E), Blatherix (ID: 17134142/0x0105723E)], work=215*
  7: 0x008B [0x03] Work_Zone[2] = 1000*
  8: 0x0090 [0x03] Work_Zone[3] = 4495*
  9: 0x0095 [0x2B] Blatherix (ID: 17134142/0x0105723E) [12574*]:
    → "No freebies this time. Trade me 10 $1 or $0 gil, you got a deal."
 10: 0x009C [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x009D [0x21] END_EVENT
 12: 0x009E [0x00] END_REQSTACK()
```

### Event 26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009F   |
| Data Size    | 43 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                               1E                 .
00A0: F0 FF FF 7F 1C 00 80 5B  02 80 3E 72 05 01 3E 72  .......[..>r..>r
00B0: 05 01 74 6C 6B 30 03 02  10 09 80 03 03 10 04 80  ..tlk0..........
00C0: 2B 3E 72 05 01 0A 80 23  21 00                    +>r....#!.      
```

#### Opcodes

```
  0: 0x009F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00A4 [0x1C] WAIT(30* ticks)
  2: 0x00A7 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Blatherix (ID: 17134142/0x0105723E), Blatherix (ID: 17134142/0x0105723E)], work=215*
  3: 0x00B6 [0x03] Work_Zone[2] = 1000*
  4: 0x00BB [0x03] Work_Zone[3] = 4495*
  5: 0x00C0 [0x2B] Blatherix (ID: 17134142/0x0105723E) [12574*]:
    → "No freebies this time. Trade me 10 $1 or $0 gil, you got a deal."
  6: 0x00C7 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00C8 [0x21] END_EVENT
  8: 0x00C9 [0x00] END_REQSTACK()
```

### Event 37

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CA   |
| Data Size    | 33 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                1E F0 FF FF 7F 1C            ......
00D0: 00 80 1D 0B 80 23 5B 02  80 3E 72 05 01 3E 72 05  .....#[..>r..>r.
00E0: 01 70 61 73 30 1D 0C 80  23 21 00                 .pas0...#!.     
```

#### Opcodes

```
  0: 0x00CA [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00CF [0x1C] WAIT(30* ticks)
  2: 0x00D2 [0x1D] PRINT_EVENT_MESSAGE(message_id=12745*)
    → "Ain't you the assistant detective working with the Mythril Musketeers?"
  3: 0x00D5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x00D6 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [Blatherix (ID: 17134142/0x0105723E), Blatherix (ID: 17134142/0x0105723E)], work=215*
  5: 0x00E5 [0x1D] PRINT_EVENT_MESSAGE(message_id=12746*)
    → "They're important customers of mine. Which means, now so are you...and I like to keep my customers happy."
  6: 0x00E8 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00E9 [0x21] END_EVENT
  8: 0x00EA [0x00] END_REQSTACK()
```

### Event 38

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EB   |
| Data Size    | 14 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                   1E F0 FF FF 7F             .....
00F0: 1C 00 80 1D 0D 80 23 21  00                       ......#!.       
```

#### Opcodes

```
  0: 0x00EB [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00F0 [0x1C] WAIT(30* ticks)
  2: 0x00F3 [0x1D] PRINT_EVENT_MESSAGE(message_id=12747*)
    → "I got all sortsa junk and gossip to trade. Keep me in mind next time you're in town."
  3: 0x00F6 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x00F7 [0x21] END_EVENT
  5: 0x00F8 [0x00] END_REQSTACK()
```

### Event 188

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F9   |
| Data Size    | 29 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                             1E F0 FF FF 7F 1C 00           .......
0100: 80 03 02 10 0E 80 03 03  10 0F 80 03 04 10 10 80  ................
0110: 1D 11 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x00F9 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00FE [0x1C] WAIT(30* ticks)
  2: 0x0101 [0x03] Work_Zone[2] = 2542*
  3: 0x0106 [0x03] Work_Zone[3] = 4543*
  4: 0x010B [0x03] Work_Zone[4] = 1241*
  5: 0x0110 [0x1D] PRINT_EVENT_MESSAGE(message_id=13186*)
    → "You bring me $0, $1, and $2, and I'll cook you up a dose of Goblin Dust. Get it? Got it? Good!"
  6: 0x0113 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0114 [0x21] END_EVENT
  8: 0x0115 [0x00] END_REQSTACK()
```

### Event 189

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0116   |
| Data Size    | 14 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                   1E F0  FF FF 7F 1C 00 80 1D 12        ..........
0120: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0116 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x011B [0x1C] WAIT(30* ticks)
  2: 0x011E [0x1D] PRINT_EVENT_MESSAGE(message_id=13187*)
    → "Headin' to the Mythril Musketeers' headquarters soon? Driftlix, or Limpears, as he's known in our circle, is ready when you are."
  3: 0x0121 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0122 [0x21] END_EVENT
  5: 0x0123 [0x00] END_REQSTACK()
```

### Event 185

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0124   |
| Data Size    | 89 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:             42 1E F0 FF  FF 7F 1C 00 80 1D 13 80      B...........
0130: 23 5B 02 80 3E 72 05 01  3E 72 05 01 74 6C 6B 30  #[..>r..>r..tlk0
0140: 1D 14 80 23 1D 15 80 23  5B 02 80 3E 72 05 01 3E  ...#...#[..>r..>
0150: 72 05 01 74 6C 6B 31 5B  02 80 3E 72 05 01 3E 72  r..tlk1[..>r..>r
0160: 05 01 70 61 73 30 1D 16  80 23 45 17 80 F0 FF FF  ..pas0...#E.....
0170: 7F F0 FF FF 7F 71 73 74  63 18 80 21 00           .....qstc..!.   
```

#### Opcodes

```
  0: 0x0124 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0125 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x012A [0x1C] WAIT(30* ticks)
  3: 0x012D [0x1D] PRINT_EVENT_MESSAGE(message_id=13190*)
    → "Oh, it's you. What's that? You wanna thank Limpears?"
  4: 0x0130 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0131 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Blatherix (ID: 17134142/0x0105723E), Blatherix (ID: 17134142/0x0105723E)], work=215*
  6: 0x0140 [0x1D] PRINT_EVENT_MESSAGE(message_id=13191*)
    → "Sorry, but you just missed him. He left here just a minute ago, skippin' along and whistlin' an old Gobbie tune. I haven't seen him so cheerful since his boss died and the business went under."
  7: 0x0143 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0144 [0x1D] PRINT_EVENT_MESSAGE(message_id=13192*)
    → "It's all thanks to the stable flow of work he's found with the Mythril Musketeers. Now that his future's secured, he can focus on the more important stuff in life, like family."
  9: 0x0147 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0148 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [Blatherix (ID: 17134142/0x0105723E), Blatherix (ID: 17134142/0x0105723E)], work=215*
 11: 0x0157 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [Blatherix (ID: 17134142/0x0105723E), Blatherix (ID: 17134142/0x0105723E)], work=215*
 12: 0x0166 [0x1D] PRINT_EVENT_MESSAGE(message_id=13193*)
    → "Seein' him happy puts a smile on my face. I know you can't see it, but I guarantee it's there. Anyway, here's a little somethin' for you, so you can share in on our delight."
 13: 0x0169 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x016A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 15: 0x017B [0x21] END_EVENT
 16: 0x017C [0x00] END_REQSTACK()
```

### Event 183

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x017D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                         00                     .  
```

#### Opcodes

```
  0: 0x017D [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x017E   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                            1F 00                ..
0180: 19 80 1A 80 1B 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x017E [0x1F] MOVE_ENTITY: EventEntity moves to X=-313.664*, Z=-43.548*, Y=-12.000*
  1: 0x0186 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0188 [0x00] END_REQSTACK()
```
