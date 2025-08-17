# 16982162 - Abda-Lurabda

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Aht Urhgan Whitegate (ID: 50) |
| Block Size       | 1216 bytes                    |
| Total Events     | 16                            |
| References Count | 32                            |

## List of Events

| Event ID                  | Entrypoint   |   Size |   Instructions |
|---------------------------|--------------|--------|----------------|
| [65535](#event-65535)     | 0x0000       |      1 |              1 |
| [257](#event-257)         | 0x0001       |     13 |              7 |
| [3050](#event-3050)       | 0x000E       |      1 |              1 |
| [65535.1](#event-65535-1) | 0x000F       |      1 |              1 |
| [65535.2](#event-65535-2) | 0x0010       |      1 |              1 |
| [65535.3](#event-65535-3) | 0x0011       |      1 |              1 |
| [65535.4](#event-65535-4) | 0x0012       |      1 |              1 |
| [65535.5](#event-65535-5) | 0x0013       |      1 |              1 |
| [265](#event-265)         | 0x0014       |      1 |              1 |
| [620](#event-620)         | 0x0015       |      1 |              1 |
| [621](#event-621)         | 0x0016       |      1 |              1 |
| [648](#event-648)         | 0x0017       |    978 |            213 |
| [900](#event-900)         | 0x03E9       |      1 |              1 |
| [901](#event-901)         | 0x03EA       |      1 |              1 |
| [902](#event-902)         | 0x03EB       |      1 |              1 |
| [905](#event-905)         | 0x03EC       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2565      |        9573 |
|       1 | 0x0000      |           0 |
|       2 | 0x0028      |          40 |
|       3 | 0x16E0      |        5856 |
|       4 | 0x16E1      |        5857 |
|       5 | 0x16E2      |        5858 |
|       6 | 0x16E3      |        5859 |
|       7 | 0x0001      |           1 |
|       8 | 0x2648      |        9800 |
|       9 | 0x16EB      |        5867 |
|      10 | 0x16E4      |        5860 |
|      11 | 0x0003      |           3 |
|      12 | 0x16E5      |        5861 |
|      13 | 0x0020      |          32 |
|      14 | 0x0002      |           2 |
|      15 | 0x16E6      |        5862 |
|      16 | 0x0021      |          33 |
|      17 | 0x16E7      |        5863 |
|      18 | 0x0004      |           4 |
|      19 | 0x16E8      |        5864 |
|      20 | 0x0005      |           5 |
|      21 | 0x16E9      |        5865 |
|      22 | 0x0006      |           6 |
|      23 | 0x16EA      |        5866 |
|      24 | 0x0012      |          18 |
|      25 | 0x0013      |          19 |
|      26 | 0x001F      |          31 |
|      27 | 0x001E      |          30 |
|      28 | 0x16EE      |        5870 |
|      29 | 0x40000000  |  1073741824 |
|      30 | 0x16EC      |        5868 |
|      31 | 0x0022      |          34 |

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

### Event 257

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 21 00         .....op...#!.  
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=9573*)
    → "Welcome to the Automaton Workshop!\u0007We're working busily-fizzily on automaton research! Well, Ghatsad is, anyway...\u007F1\u0000\u0007"
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x21] END_EVENT
  6: 0x000D [0x00] END_REQSTACK()
```

### Event 3050

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            00                   . 
```

#### Opcodes

```
  0: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               00                 .
```

#### Opcodes

```
  0: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0010  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    00                                              .              
```

#### Opcodes

```
  0: 0x0011 [0x00] END_REQSTACK()
```

### Event 65535.4

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

### Event 65535.5

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

### Event 265

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

### Event 620

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0015  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                00                                      .          
```

#### Opcodes

```
  0: 0x0015 [0x00] END_REQSTACK()
```

### Event 621

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0016  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   00                                    .         
```

#### Opcodes

```
  0: 0x0016 [0x00] END_REQSTACK()
```

### Event 648

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0017    |
| Data Size    | 978 bytes |
| Instructions | 160       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      03  01 10 01 80 1E F0 FF FF         .........
0020: 7F 6F 70 66 02 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  .opf..........tl
0030: 6B 30 1D 03 80 23 1D 04  80 23 1D 05 80 23 24 06  k0...#...#...#$.
0040: 80 07 80 01 80 25 02 00  10 01 80 00 CD 03 02 04  .....%..........
0050: 10 08 80 03 5D 00 1D 09  80 23 01 CA 03 1D 0A 80  ....]....#......
0060: 23 40 01 80 0B 80 01 10  07 80 24 0C 80 01 80 01  #@........$.....
0070: 80 25 02 00 10 0D 80 00  60 03 40 01 80 0B 80 01  .%......`.@.....
0080: 10 0E 80 24 0F 80 01 80  01 80 25 02 00 10 0D 80  ...$......%.....
0090: 00 99 00 01 61 00 01 FD  02 02 00 10 10 80 00 F2  ....a...........
00A0: 02 40 01 80 0B 80 01 10  0B 80 24 11 80 01 80 01  .@........$.....
00B0: 80 25 02 00 10 0D 80 00  C0 00 01 7A 00 01 8F 02  .%.........z....
00C0: 02 00 10 10 80 00 84 02  40 01 80 0B 80 01 10 12  ........@.......
00D0: 80 24 13 80 01 80 01 80  25 02 00 10 0D 80 00 E7  .$......%.......
00E0: 00 01 A1 00 01 21 02 02  00 10 10 80 00 16 02 40  .....!.........@
00F0: 01 80 0B 80 01 10 14 80  24 15 80 01 80 01 80 25  ........$......%
0100: 02 00 10 0D 80 00 0E 01  01 C8 00 01 B3 01 02 00  ................
0110: 10 10 80 00 A8 01 40 01  80 0B 80 01 10 16 80 24  ......@........$
0120: 17 80 01 80 01 80 25 02  00 10 18 80 00 35 01 01  ......%......5..
0130: EF 00 01 45 01 02 00 10  19 80 00 45 01 03 00 10  ...E.......E....
0140: 0D 80 01 45 01 3E 01 10  1A 80 4F 01 01 A5 01 02  ...E.>....O.....
0150: 00 10 18 80 03 A5 01 42  3C 01 10 1A 80 07 80 40  .......B<......@
0160: 12 80 1B 80 01 10 00 10  24 1C 80 07 80 01 80 25  ........$......%
0170: 02 00 10 01 80 00 7C 01  42 01 A1 01 02 00 10 07  ......|.B.......
0180: 80 00 8F 01 03 01 10 01  80 01 61 00 01 A1 01 02  ..........a.....
0190: 00 10 0E 80 00 A1 01 03  01 10 1D 80 21 00 01 A1  ............!...
01A0: 01 1D 1E 80 23 01 B3 01  02 00 10 1F 80 00 B3 01  ....#...........
01B0: 01 B3 01 3E 01 10 1A 80  BD 01 01 13 02 02 00 10  ...>............
01C0: 0D 80 03 13 02 42 3C 01  10 1A 80 07 80 40 12 80  .....B<......@..
01D0: 1B 80 01 10 00 10 24 1C  80 07 80 01 80 25 02 00  ......$......%..
01E0: 10 01 80 00 EA 01 42 01  0F 02 02 00 10 07 80 00  ......B.........
01F0: FD 01 03 01 10 01 80 01  61 00 01 0F 02 02 00 10  ........a.......
0200: 0E 80 00 0F 02 03 01 10  1D 80 21 00 01 0F 02 1D  ..........!.....
0210: 1E 80 23 01 21 02 02 00  10 1F 80 00 21 02 01 21  ..#.!.......!..!
0220: 02 3E 01 10 1A 80 2B 02  01 81 02 02 00 10 0D 80  .>....+.........
0230: 03 81 02 42 3C 01 10 1A  80 07 80 40 12 80 1B 80  ...B<......@....
0240: 01 10 00 10 24 1C 80 07  80 01 80 25 02 00 10 01  ....$......%....
0250: 80 00 58 02 42 01 7D 02  02 00 10 07 80 00 6B 02  ..X.B.}.......k.
0260: 03 01 10 01 80 01 61 00  01 7D 02 02 00 10 0E 80  ......a..}......
0270: 00 7D 02 03 01 10 1D 80  21 00 01 7D 02 1D 1E 80  .}......!..}....
0280: 23 01 8F 02 02 00 10 1F  80 00 8F 02 01 8F 02 3E  #..............>
0290: 01 10 1A 80 99 02 01 EF  02 02 00 10 0D 80 03 EF  ................
02A0: 02 42 3C 01 10 1A 80 07  80 40 12 80 1B 80 01 10  .B<......@......
02B0: 00 10 24 1C 80 07 80 01  80 25 02 00 10 01 80 00  ..$......%......
02C0: C6 02 42 01 EB 02 02 00  10 07 80 00 D9 02 03 01  ..B.............
02D0: 10 01 80 01 61 00 01 EB  02 02 00 10 0E 80 00 EB  ....a...........
02E0: 02 03 01 10 1D 80 21 00  01 EB 02 1D 1E 80 23 01  ......!.......#.
02F0: FD 02 02 00 10 1F 80 00  FD 02 01 FD 02 3E 01 10  .............>..
0300: 1A 80 07 03 01 5D 03 02  00 10 0D 80 03 5D 03 42  .....].......].B
0310: 3C 01 10 1A 80 07 80 40  12 80 1B 80 01 10 00 10  <......@........
0320: 24 1C 80 07 80 01 80 25  02 00 10 01 80 00 34 03  $......%......4.
0330: 42 01 59 03 02 00 10 07  80 00 47 03 03 01 10 01  B.Y.......G.....
0340: 80 01 61 00 01 59 03 02  00 10 0E 80 00 59 03 03  ..a..Y.......Y..
0350: 01 10 1D 80 21 00 01 59  03 1D 1E 80 23 01 6B 03  ....!..Y....#.k.
0360: 02 00 10 10 80 00 6B 03  01 6B 03 3E 01 10 1A 80  ......k..k.>....
0370: 75 03 01 CA 03 02 00 10  0D 80 03 CA 03 3C 01 10  u............<..
0380: 1A 80 07 80 40 12 80 1B  80 01 10 00 10 24 1C 80  ....@........$..
0390: 07 80 01 80 25 02 00 10  01 80 00 A1 03 42 01 C6  ....%........B..
03A0: 03 02 00 10 07 80 00 B4  03 03 01 10 01 80 01 61  ...............a
03B0: 00 01 C6 03 02 00 10 0E  80 00 C6 03 03 01 10 1D  ................
03C0: 80 21 00 01 C6 03 1D 1E  80 23 01 D8 03 02 00 10  .!.......#......
03D0: 07 80 00 D8 03 01 D8 03  66 02 80 F8 FF FF 7F F8  ........f.......
03E0: FF FF 7F 74 6C 6B 31 21  00                       ...tlk1!.       
```

#### Opcodes

```
  0: 0x0017 [0x03] Work_Zone[1] = 0*
  1: 0x001C [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0021 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0022 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0023 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  5: 0x0032 [0x1D] PRINT_EVENT_MESSAGE(message_id=5856*)
    → "You're a puppetmaster, right?\u0007Come on, anyone can tell!\u007F1\u0000\u0007"
  6: 0x0035 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0036 [0x1D] PRINT_EVENT_MESSAGE(message_id=5857*)
    → "What's your automaton's name?\u007F1\u0000\u0007"
  8: 0x0039 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x003A [0x1D] PRINT_EVENT_MESSAGE(message_id=5858*)
    → "If you'd rather name it something different, just pay me 
\u0001 gil and I'll help you out!\u007F1\u0000\u0007"
 10: 0x003D [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x003E [0x24] CREATE_DIALOG(message_id=5859*, default_option=1*, option_flags=0*)
    → "Rename your automaton?\u0007\u000BI would love to.\u0007No thanks.\u007F1\u0000\u0007"
 12: 0x0045 [0x25] WAIT_DIALOG_SELECT()
 13: 0x0046 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x03CD
 14: 0x004E [0x02] IF !(Work_Zone[4] >= 9800*) GOTO 0x005D
 15: 0x0056 [0x1D] PRINT_EVENT_MESSAGE(message_id=5867*)
    → "You don't have enough gil! Get lost!\u007F1\u0000\u0007"
 16: 0x0059 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x005A [0x01] GOTO 0x03CA
 18: 0x005D [0x1D] PRINT_EVENT_MESSAGE(message_id=5860*)
    → "Hmmm... How about one of these?\u007F1\u0000\u0007"
 19: 0x0060 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0061:
 20: 0x0061 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=3*, target=Work_Zone[1], source=1*)
 21: 0x006A [0x24] CREATE_DIALOG(message_id=5861*, default_option=0*, option_flags=0*)
    → "Choose your automaton's name.\u0007\u000BLuron\u0007Drille\u0007Tournefoux\u0007Chafouin\u0007Plaisantin\u0007Loustic\u0007Histrion\u0007Bobeche\u0007Bougrion\u0007Rouleteau\u0007Allouette\u0007Serenade\u0007Ficelette\u0007Tocadie\u0007Caprice\u0007Foucade\u0007Capillotte\u0007Quenotte\u0007Pacotille\u0007Comedie\u0007Kagekiyo\u0007Toraoh\u0007Genta\u0007Kintoki\u0007Koumei\u0007Pamama\u0007Lobo\u0007Tsukushi\u0007Oniwaka\u0007Kenbishi\u0007Hannya\u0007Mashira\u0007View more.\u0007Cancel.\u007F1\u0000\u0007"
 22: 0x0071 [0x25] WAIT_DIALOG_SELECT()
 23: 0x0072 [0x02] IF !(Work_Zone[0] == 32*) GOTO 0x0360

SUBROUTINE_007A:
 24: 0x007A [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=3*, target=Work_Zone[1], source=2*)
 25: 0x0083 [0x24] CREATE_DIALOG(message_id=5862*, default_option=0*, option_flags=0*)
    → "Choose your automaton's name.\u0007\u000BNadeshiko\u0007E100\u0007Koume\u0007X-32\u0007Poppo\u0007Asuka\u0007Sakura\u0007Tao\u0007Mao\u0007Gadget\u0007Marion\u0007Widget\u0007Quirk\u0007Sprocket\u0007Cogette\u0007Lecter\u0007Coppelia\u0007Sparky\u0007Clank\u0007Calcobrena\u0007Crackle\u0007Ricochet\u0007Josette\u0007Fritz\u0007Skippy\u0007Pino\u0007Mandarin\u0007Jackstraw\u0007Guignol\u0007Moppet\u0007Nutcracker\u0007Erwin\u0007View previous.\u0007View more.\u0007Cancel.\u007F1\u0000\u0007"
 26: 0x008A [0x25] WAIT_DIALOG_SELECT()
 27: 0x008B [0x02] IF !(Work_Zone[0] == 32*) GOTO 0x0099
 28: 0x0093 [0x01] GOTO 0x0061

SUBROUTINE_00A1:
 29: 0x00A1 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=3*, target=Work_Zone[1], source=3*)
 30: 0x00AA [0x24] CREATE_DIALOG(message_id=5863*, default_option=0*, option_flags=0*)
    → "Choose your automaton's name.\u0007\u000BOtto\u0007Gustav\u0007Muffin\u0007Xaver\u0007Toni\u0007Ina\u0007Gerda\u0007Petra\u0007Verena\u0007Rosi\u0007Schatzi\u0007Warashi\u0007Klingel\u0007Clochette\u0007Campanello\u0007Kaiserin\u0007Principessa\u0007Butler\u0007Graf\u0007Caro\u0007Cara\u0007Mademoiselle\u0007Herzog\u0007Tramp\u0007V-1000\u0007Hikozaemon\u0007Nine\u0007Acht\u0007Quattro\u0007Zero\u0007Dreizehn\u0007Seize\u0007View previous.\u0007View more.\u0007Cancel.\u007F1\u0000\u0007"
 31: 0x00B1 [0x25] WAIT_DIALOG_SELECT()
 32: 0x00B2 [0x02] IF !(Work_Zone[0] == 32*) GOTO 0x00C0
 33: 0x00BA [0x01] GOTO 0x007A

SUBROUTINE_00C8:
 34: 0x00C8 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=3*, target=Work_Zone[1], source=4*)
 35: 0x00D1 [0x24] CREATE_DIALOG(message_id=5864*, default_option=0*, option_flags=0*)
    → "Choose your automaton's name.\u0007\u000BFukusuke\u0007Mataemon\u0007Kansuke\u0007Polichinelle\u0007Tobisuke\u0007Sasuke\u0007Shijimi\u0007Chobi\u0007Aurelie\u0007Magalie\u0007Aurore\u0007Caroline\u0007Andrea\u0007Machinette\u0007Clarine\u0007Armelle\u0007Reinette\u0007Dorlote\u0007Turlupin\u0007Klaxon\u0007Bambino\u0007Potiron\u0007Fustige\u0007Amidon\u0007Machin\u0007Bidulon\u0007Tandem\u0007Prestidige\u0007Purute-Porute\u0007Bito-Rabito\u0007Cocoa\u0007Totomo\u0007View previous.\u0007View more.\u0007Cancel.\u007F1\u0000\u0007"
 36: 0x00D8 [0x25] WAIT_DIALOG_SELECT()
 37: 0x00D9 [0x02] IF !(Work_Zone[0] == 32*) GOTO 0x00E7
 38: 0x00E1 [0x01] GOTO 0x00A1

SUBROUTINE_00EF:
 39: 0x00EF [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=3*, target=Work_Zone[1], source=5*)
 40: 0x00F8 [0x24] CREATE_DIALOG(message_id=5865*, default_option=0*, option_flags=0*)
    → "Choose your automaton's name.\u0007\u000BCenturion\u0007A7V\u0007Scipio\u0007Sentinel\u0007Pioneer\u0007Seneschal\u0007Ginjin\u0007Amagatsu\u0007Dolly\u0007Fantoccini\u0007Joe\u0007Kikizaru\u0007Whippet\u0007Punchinello\u0007Charlie\u0007Midge\u0007Petrouchka\u0007Schneider\u0007Ushabti\u0007Noel\u0007Yajirobe\u0007Hina\u0007Nora\u0007Shoki\u0007Kobina\u0007Kokeshi\u0007Mame\u0007Bishop\u0007Marvin\u0007Dora\u0007Data\u0007Robin\u0007View previous.\u0007View more.\u0007Cancel.\u007F1\u0000\u0007"
 41: 0x00FF [0x25] WAIT_DIALOG_SELECT()
 42: 0x0100 [0x02] IF !(Work_Zone[0] == 32*) GOTO 0x010E
 43: 0x0108 [0x01] GOTO 0x00C8

SUBROUTINE_0145:
 44: 0x0145 [0x3E] IF !(Work_Zone[1] bit 31*) GOTO 0x014F
 45: 0x014C [0x01] GOTO 0x01A5
 46: 0x014F [0x02] IF !(Work_Zone[0] >= 18*) GOTO 0x01A5
 47: 0x0157 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 48: 0x0158 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=Work_Zone[1], bit_index_work_offset=31*, condition_work_offset=1*)
 49: 0x015F [0x40] SET_BIT_WORK_RANGE(start_bit=4*, end_bit=30*, target=Work_Zone[1], source=Work_Zone[0])
 50: 0x0168 [0x24] CREATE_DIALOG(message_id=5870*, default_option=1*, option_flags=0*)
    → "Are you sure this name is okay?\u0007\u000BYes, this is it.\u0007On second thought...\u0007Cancel.\u007F1\u0000\u0007"
 51: 0x016F [0x25] WAIT_DIALOG_SELECT()
 52: 0x0170 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x017C
 53: 0x0178 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 54: 0x0179 [0x01] GOTO 0x01A1
 55: 0x017C [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x018F
 56: 0x0184 [0x03] Work_Zone[1] = 0*
 57: 0x0189 [0x01] GOTO 0x0061

SUBROUTINE_01A1:
 58: 0x01A1 [0x1D] PRINT_EVENT_MESSAGE(message_id=5868*)
    → "Oh, nice choice!\u0007Congratulations on your new name!\u007F1\u0000\u0007"
 59: 0x01A4 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_01A5:
 60: 0x01A5 [0x01] GOTO 0x01B3
 61: 0x01A8 [0x02] IF !(Work_Zone[0] == 34*) GOTO 0x01B3
 62: 0x01B0 [0x01] GOTO 0x01B3

SUBROUTINE_01B3:
 63: 0x01B3 [0x3E] IF !(Work_Zone[1] bit 31*) GOTO 0x01BD
 64: 0x01BA [0x01] GOTO 0x0213
 65: 0x01BD [0x02] IF !(Work_Zone[0] >= 32*) GOTO 0x0213
 66: 0x01C5 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 67: 0x01C6 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=Work_Zone[1], bit_index_work_offset=31*, condition_work_offset=1*)
 68: 0x01CD [0x40] SET_BIT_WORK_RANGE(start_bit=4*, end_bit=30*, target=Work_Zone[1], source=Work_Zone[0])
 69: 0x01D6 [0x24] CREATE_DIALOG(message_id=5870*, default_option=1*, option_flags=0*)
    → "Are you sure this name is okay?\u0007\u000BYes, this is it.\u0007On second thought...\u0007Cancel.\u007F1\u0000\u0007"
 70: 0x01DD [0x25] WAIT_DIALOG_SELECT()
 71: 0x01DE [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01EA
 72: 0x01E6 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 73: 0x01E7 [0x01] GOTO 0x020F
 74: 0x01EA [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01FD
 75: 0x01F2 [0x03] Work_Zone[1] = 0*
 76: 0x01F7 [0x01] GOTO 0x0061

SUBROUTINE_020F:
 77: 0x020F [0x1D] PRINT_EVENT_MESSAGE(message_id=5868*)
    → "Oh, nice choice!\u0007Congratulations on your new name!\u007F1\u0000\u0007"
 78: 0x0212 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0213:
 79: 0x0213 [0x01] GOTO 0x0221
 80: 0x0216 [0x02] IF !(Work_Zone[0] == 34*) GOTO 0x0221
 81: 0x021E [0x01] GOTO 0x0221

SUBROUTINE_0221:
 82: 0x0221 [0x3E] IF !(Work_Zone[1] bit 31*) GOTO 0x022B
 83: 0x0228 [0x01] GOTO 0x0281
 84: 0x022B [0x02] IF !(Work_Zone[0] >= 32*) GOTO 0x0281
 85: 0x0233 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 86: 0x0234 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=Work_Zone[1], bit_index_work_offset=31*, condition_work_offset=1*)
 87: 0x023B [0x40] SET_BIT_WORK_RANGE(start_bit=4*, end_bit=30*, target=Work_Zone[1], source=Work_Zone[0])
 88: 0x0244 [0x24] CREATE_DIALOG(message_id=5870*, default_option=1*, option_flags=0*)
    → "Are you sure this name is okay?\u0007\u000BYes, this is it.\u0007On second thought...\u0007Cancel.\u007F1\u0000\u0007"
 89: 0x024B [0x25] WAIT_DIALOG_SELECT()
 90: 0x024C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0258
 91: 0x0254 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 92: 0x0255 [0x01] GOTO 0x027D
 93: 0x0258 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x026B
 94: 0x0260 [0x03] Work_Zone[1] = 0*
 95: 0x0265 [0x01] GOTO 0x0061

SUBROUTINE_027D:
 96: 0x027D [0x1D] PRINT_EVENT_MESSAGE(message_id=5868*)
    → "Oh, nice choice!\u0007Congratulations on your new name!\u007F1\u0000\u0007"
 97: 0x0280 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0281:
 98: 0x0281 [0x01] GOTO 0x028F
 99: 0x0284 [0x02] IF !(Work_Zone[0] == 34*) GOTO 0x028F
100: 0x028C [0x01] GOTO 0x028F

SUBROUTINE_028F:
101: 0x028F [0x3E] IF !(Work_Zone[1] bit 31*) GOTO 0x0299
102: 0x0296 [0x01] GOTO 0x02EF
103: 0x0299 [0x02] IF !(Work_Zone[0] >= 32*) GOTO 0x02EF
104: 0x02A1 [0x42] SET_CLI_EVENT_CANCEL_DATA()
105: 0x02A2 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=Work_Zone[1], bit_index_work_offset=31*, condition_work_offset=1*)
106: 0x02A9 [0x40] SET_BIT_WORK_RANGE(start_bit=4*, end_bit=30*, target=Work_Zone[1], source=Work_Zone[0])
107: 0x02B2 [0x24] CREATE_DIALOG(message_id=5870*, default_option=1*, option_flags=0*)
    → "Are you sure this name is okay?\u0007\u000BYes, this is it.\u0007On second thought...\u0007Cancel.\u007F1\u0000\u0007"
108: 0x02B9 [0x25] WAIT_DIALOG_SELECT()
109: 0x02BA [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x02C6
110: 0x02C2 [0x42] SET_CLI_EVENT_CANCEL_DATA()
111: 0x02C3 [0x01] GOTO 0x02EB
112: 0x02C6 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x02D9
113: 0x02CE [0x03] Work_Zone[1] = 0*
114: 0x02D3 [0x01] GOTO 0x0061

SUBROUTINE_02EB:
115: 0x02EB [0x1D] PRINT_EVENT_MESSAGE(message_id=5868*)
    → "Oh, nice choice!\u0007Congratulations on your new name!\u007F1\u0000\u0007"
116: 0x02EE [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_02EF:
117: 0x02EF [0x01] GOTO 0x02FD
118: 0x02F2 [0x02] IF !(Work_Zone[0] == 34*) GOTO 0x02FD
119: 0x02FA [0x01] GOTO 0x02FD

SUBROUTINE_02FD:
120: 0x02FD [0x3E] IF !(Work_Zone[1] bit 31*) GOTO 0x0307
121: 0x0304 [0x01] GOTO 0x035D
122: 0x0307 [0x02] IF !(Work_Zone[0] >= 32*) GOTO 0x035D
123: 0x030F [0x42] SET_CLI_EVENT_CANCEL_DATA()
124: 0x0310 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=Work_Zone[1], bit_index_work_offset=31*, condition_work_offset=1*)
125: 0x0317 [0x40] SET_BIT_WORK_RANGE(start_bit=4*, end_bit=30*, target=Work_Zone[1], source=Work_Zone[0])
126: 0x0320 [0x24] CREATE_DIALOG(message_id=5870*, default_option=1*, option_flags=0*)
    → "Are you sure this name is okay?\u0007\u000BYes, this is it.\u0007On second thought...\u0007Cancel.\u007F1\u0000\u0007"
127: 0x0327 [0x25] WAIT_DIALOG_SELECT()
128: 0x0328 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0334
129: 0x0330 [0x42] SET_CLI_EVENT_CANCEL_DATA()
130: 0x0331 [0x01] GOTO 0x0359
131: 0x0334 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0347
132: 0x033C [0x03] Work_Zone[1] = 0*
133: 0x0341 [0x01] GOTO 0x0061

SUBROUTINE_0359:
134: 0x0359 [0x1D] PRINT_EVENT_MESSAGE(message_id=5868*)
    → "Oh, nice choice!\u0007Congratulations on your new name!\u007F1\u0000\u0007"
135: 0x035C [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_035D:
136: 0x035D [0x01] GOTO 0x036B
137: 0x0360 [0x02] IF !(Work_Zone[0] == 33*) GOTO 0x036B
138: 0x0368 [0x01] GOTO 0x036B

SUBROUTINE_036B:
139: 0x036B [0x3E] IF !(Work_Zone[1] bit 31*) GOTO 0x0375
140: 0x0372 [0x01] GOTO 0x03CA
141: 0x0375 [0x02] IF !(Work_Zone[0] >= 32*) GOTO 0x03CA
142: 0x037D [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=Work_Zone[1], bit_index_work_offset=31*, condition_work_offset=1*)
143: 0x0384 [0x40] SET_BIT_WORK_RANGE(start_bit=4*, end_bit=30*, target=Work_Zone[1], source=Work_Zone[0])
144: 0x038D [0x24] CREATE_DIALOG(message_id=5870*, default_option=1*, option_flags=0*)
    → "Are you sure this name is okay?\u0007\u000BYes, this is it.\u0007On second thought...\u0007Cancel.\u007F1\u0000\u0007"
145: 0x0394 [0x25] WAIT_DIALOG_SELECT()
146: 0x0395 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x03A1
147: 0x039D [0x42] SET_CLI_EVENT_CANCEL_DATA()
148: 0x039E [0x01] GOTO 0x03C6
149: 0x03A1 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x03B4
150: 0x03A9 [0x03] Work_Zone[1] = 0*
151: 0x03AE [0x01] GOTO 0x0061

SUBROUTINE_03C6:
152: 0x03C6 [0x1D] PRINT_EVENT_MESSAGE(message_id=5868*)
    → "Oh, nice choice!\u0007Congratulations on your new name!\u007F1\u0000\u0007"
153: 0x03C9 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_03CA:
154: 0x03CA [0x01] GOTO 0x03D8
155: 0x03CD [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x03D8
156: 0x03D5 [0x01] GOTO 0x03D8

SUBROUTINE_03D8:
157: 0x03D8 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
158: 0x03E7 [0x21] END_EVENT
159: 0x03E8 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0096 [0x01] GOTO 0x02FD
# Dead code (unreachable instructions):
     0x00BD [0x01] GOTO 0x028F
# Dead code (unreachable instructions):
     0x00E4 [0x01] GOTO 0x0221
# Dead code (unreachable instructions):
     0x010B [0x01] GOTO 0x01B3
     0x0132 [0x01] GOTO 0x0145
# Dead code (unreachable instructions):
     0x018C [0x01] GOTO 0x01A1
     0x019E [0x01] GOTO 0x01A1
# Dead code (unreachable instructions):
     0x01FA [0x01] GOTO 0x020F
     0x020C [0x01] GOTO 0x020F
# Dead code (unreachable instructions):
     0x0268 [0x01] GOTO 0x027D
     0x027A [0x01] GOTO 0x027D
# Dead code (unreachable instructions):
     0x02D6 [0x01] GOTO 0x02EB
     0x02E8 [0x01] GOTO 0x02EB
# Dead code (unreachable instructions):
     0x0344 [0x01] GOTO 0x0359
     0x0356 [0x01] GOTO 0x0359
# Dead code (unreachable instructions):
     0x03B1 [0x01] GOTO 0x03C6
     0x03C3 [0x01] GOTO 0x03C6
```

### Event 900

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03E9  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03E0:                             00                             .      
```

#### Opcodes

```
  0: 0x03E9 [0x00] END_REQSTACK()
```

### Event 901

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03EA  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03E0:                                00                           .     
```

#### Opcodes

```
  0: 0x03EA [0x00] END_REQSTACK()
```

### Event 902

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03EB  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03E0:                                   00                         .    
```

#### Opcodes

```
  0: 0x03EB [0x00] END_REQSTACK()
```

### Event 905

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03EC  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03E0:                                      00                       .   
```

#### Opcodes

```
  0: 0x03EC [0x00] END_REQSTACK()
```
