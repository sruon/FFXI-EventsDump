# 17723595 - Talking Doll

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 876 bytes                     |
| Total Events     | 7                             |
| References Count | 48                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [709](#event-709)        | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |    422 |             71 |
| [65535.2](#event-655352) | 0x01AE       |     10 |              2 |
| [65535.3](#event-655353) | 0x01B8       |    119 |             21 |
| [65535.4](#event-655354) | 0x022F       |     75 |             14 |
| [65535.5](#event-655355) | 0x027A       |      6 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0003      |           3 |
|       1 | 0x0001      |           1 |
|       2 | 0x8CCE      |       36046 |
|       3 | 0xFFFF62FA  |  4294927098 |
|       4 | 0x1B58      |        7000 |
|       5 | 0x0760      |        1888 |
|       6 | 0x0004      |           4 |
|       7 | 0xFFFD2C44  |  4294782020 |
|       8 | 0x1A7F3     |      108531 |
|       9 | 0xFFFFFCE0  |  4294966496 |
|      10 | 0x0941      |        2369 |
|      11 | 0x0005      |           5 |
|      12 | 0x6FBF      |       28607 |
|      13 | 0xE4BD      |       58557 |
|      14 | 0xFFFFBE47  |  4294950471 |
|      15 | 0x03CE      |         974 |
|      16 | 0x8CF2      |       36082 |
|      17 | 0xFFFF6260  |  4294926944 |
|      18 | 0x1F40      |        8000 |
|      19 | 0x0190      |         400 |
|      20 | 0xFFFFC22F  |  4294951471 |
|      21 | 0x0006      |           6 |
|      22 | 0x0008      |           8 |
|      23 | 0xFFFFFF38  |  4294967096 |
|      24 | 0xFFFFC03B  |  4294950971 |
|      25 | 0x5C76      |       23670 |
|      26 | 0x7E84      |       32388 |
|      27 | 0xFFFFB89E  |  4294949022 |
|      28 | 0x05B3      |        1459 |
|      29 | 0x0032      |          50 |
|      30 | 0x5A12      |       23058 |
|      31 | 0x7A7E      |       31358 |
|      32 | 0xFFFFB4FA  |  4294948090 |
|      33 | 0x0615      |        1557 |
|      34 | 0x0064      |         100 |
|      35 | 0x00C8      |         200 |
|      36 | 0x012C      |         300 |
|      37 | 0x0000      |           0 |
|      38 | 0x5BFB      |       23547 |
|      39 | 0x72CF      |       29391 |
|      40 | 0xFFFFB4D7  |  4294948055 |
|      41 | 0x0B82      |        2946 |
|      42 | 0x6119      |       24857 |
|      43 | 0x786F      |       30831 |
|      44 | 0xFFFFB87C  |  4294948988 |
|      45 | 0x05C0      |        1472 |
|      46 | 0x000A      |          10 |
|      47 | 0x0096      |         150 |

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

### Event 709

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0008    |
| Data Size    | 422 bytes |
| Instructions | 71        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          02 09 10 00 80 80 50 00          ......P.
0010: 33 01 02 04 10 01 80 00  26 00 37 02 80 03 80 04  3.......&.7.....
0020: 80 05 80 01 4B 00 02 04  10 06 80 00 3A 00 37 07  ....K.......:.7.
0030: 80 08 80 09 80 0A 80 01  4B 00 02 04 10 0B 80 00  ........K.......
0040: 4B 00 37 0C 80 0D 80 0E  80 0F 80 33 01 01 AD 01  K.7........3....
0050: 02 09 10 06 80 80 98 00  33 01 02 04 10 01 80 00  ........3.......
0060: 6E 00 37 02 80 03 80 04  80 05 80 01 93 00 02 04  n.7.............
0070: 10 06 80 00 82 00 37 07  80 08 80 09 80 0A 80 01  ......7.........
0080: 93 00 02 04 10 0B 80 00  93 00 37 0C 80 0D 80 0E  ..........7.....
0090: 80 0F 80 33 01 01 AD 01  02 09 10 0B 80 80 E0 00  ...3............
00A0: 33 01 02 04 10 01 80 00  B6 00 37 10 80 11 80 12  3.........7.....
00B0: 80 05 80 01 DB 00 02 04  10 06 80 00 CA 00 37 07  ..............7.
00C0: 80 08 80 13 80 0A 80 01  DB 00 02 04 10 0B 80 00  ................
00D0: DB 00 37 0C 80 0D 80 14  80 0F 80 33 01 01 AD 01  ..7........3....
00E0: 02 09 10 15 80 80 28 01  33 01 02 04 10 01 80 00  ......(.3.......
00F0: FE 00 37 10 80 11 80 12  80 05 80 01 23 01 02 04  ..7.........#...
0100: 10 06 80 00 12 01 37 07  80 08 80 13 80 0A 80 01  ......7.........
0110: 23 01 02 04 10 0B 80 00  23 01 37 0C 80 0D 80 14  #.......#.7.....
0120: 80 0F 80 33 01 01 AD 01  02 09 10 16 80 80 70 01  ...3..........p.
0130: 33 01 02 04 10 01 80 00  46 01 37 02 80 03 80 04  3.......F.7.....
0140: 80 05 80 01 6B 01 02 04  10 06 80 00 5A 01 37 07  ....k.......Z.7.
0150: 80 08 80 09 80 0A 80 01  6B 01 02 04 10 0B 80 00  ........k.......
0160: 6B 01 37 0C 80 0D 80 0E  80 0F 80 33 01 01 AD 01  k.7........3....
0170: 33 01 02 04 10 01 80 00  86 01 37 10 80 11 80 04  3.........7.....
0180: 80 05 80 01 AB 01 02 04  10 06 80 00 9A 01 37 07  ..............7.
0190: 80 08 80 17 80 0A 80 01  AB 01 02 04 10 0B 80 00  ................
01A0: AB 01 37 0C 80 0D 80 18  80 0F 80 33 01 00        ..7........3..  
```

#### Opcodes

```
  0: 0x0008 [0x02] IF !(Work_Zone[9] == 3*) GOTO 0x0050
  1: 0x0010 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  2: 0x0012 [0x02] IF !(Work_Zone[4] == 1*) GOTO 0x0026
  3: 0x001A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=36.046*, z=-40.198*, y=7.000*, direction=165.9°*
  4: 0x0023 [0x01] GOTO 0x004B
  5: 0x0026 [0x02] IF !(Work_Zone[4] == 4*) GOTO 0x003A
  6: 0x002E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-185.276*, z=108.531*, y=-0.800*, direction=208.2°*
  7: 0x0037 [0x01] GOTO 0x004B
  8: 0x003A [0x02] IF !(Work_Zone[4] == 5*) GOTO 0x004B
  9: 0x0042 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=28.607*, z=58.557*, y=-16.825*, direction=85.6°*

SUBROUTINE_004B:
 10: 0x004B [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
 11: 0x004D [0x01] GOTO 0x01AD
 12: 0x0050 [0x02] IF !(Work_Zone[9] == 4*) GOTO 0x0098
 13: 0x0058 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
 14: 0x005A [0x02] IF !(Work_Zone[4] == 1*) GOTO 0x006E
 15: 0x0062 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=36.046*, z=-40.198*, y=7.000*, direction=165.9°*
 16: 0x006B [0x01] GOTO 0x0093
 17: 0x006E [0x02] IF !(Work_Zone[4] == 4*) GOTO 0x0082
 18: 0x0076 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-185.276*, z=108.531*, y=-0.800*, direction=208.2°*
 19: 0x007F [0x01] GOTO 0x0093
 20: 0x0082 [0x02] IF !(Work_Zone[4] == 5*) GOTO 0x0093
 21: 0x008A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=28.607*, z=58.557*, y=-16.825*, direction=85.6°*

SUBROUTINE_0093:
 22: 0x0093 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
 23: 0x0095 [0x01] GOTO 0x01AD
 24: 0x0098 [0x02] IF !(Work_Zone[9] == 5*) GOTO 0x00E0
 25: 0x00A0 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
 26: 0x00A2 [0x02] IF !(Work_Zone[4] == 1*) GOTO 0x00B6
 27: 0x00AA [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=36.082*, z=-40.352*, y=8.000*, direction=165.9°*
 28: 0x00B3 [0x01] GOTO 0x00DB
 29: 0x00B6 [0x02] IF !(Work_Zone[4] == 4*) GOTO 0x00CA
 30: 0x00BE [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-185.276*, z=108.531*, y=0.400*, direction=208.2°*
 31: 0x00C7 [0x01] GOTO 0x00DB
 32: 0x00CA [0x02] IF !(Work_Zone[4] == 5*) GOTO 0x00DB
 33: 0x00D2 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=28.607*, z=58.557*, y=-15.825*, direction=85.6°*

SUBROUTINE_00DB:
 34: 0x00DB [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
 35: 0x00DD [0x01] GOTO 0x01AD
 36: 0x00E0 [0x02] IF !(Work_Zone[9] == 6*) GOTO 0x0128
 37: 0x00E8 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
 38: 0x00EA [0x02] IF !(Work_Zone[4] == 1*) GOTO 0x00FE
 39: 0x00F2 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=36.082*, z=-40.352*, y=8.000*, direction=165.9°*
 40: 0x00FB [0x01] GOTO 0x0123
 41: 0x00FE [0x02] IF !(Work_Zone[4] == 4*) GOTO 0x0112
 42: 0x0106 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-185.276*, z=108.531*, y=0.400*, direction=208.2°*
 43: 0x010F [0x01] GOTO 0x0123
 44: 0x0112 [0x02] IF !(Work_Zone[4] == 5*) GOTO 0x0123
 45: 0x011A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=28.607*, z=58.557*, y=-15.825*, direction=85.6°*

SUBROUTINE_0123:
 46: 0x0123 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
 47: 0x0125 [0x01] GOTO 0x01AD
 48: 0x0128 [0x02] IF !(Work_Zone[9] == 8*) GOTO 0x0170
 49: 0x0130 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
 50: 0x0132 [0x02] IF !(Work_Zone[4] == 1*) GOTO 0x0146
 51: 0x013A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=36.046*, z=-40.198*, y=7.000*, direction=165.9°*
 52: 0x0143 [0x01] GOTO 0x016B
 53: 0x0146 [0x02] IF !(Work_Zone[4] == 4*) GOTO 0x015A
 54: 0x014E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-185.276*, z=108.531*, y=-0.800*, direction=208.2°*
 55: 0x0157 [0x01] GOTO 0x016B
 56: 0x015A [0x02] IF !(Work_Zone[4] == 5*) GOTO 0x016B
 57: 0x0162 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=28.607*, z=58.557*, y=-16.825*, direction=85.6°*

SUBROUTINE_016B:
 58: 0x016B [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
 59: 0x016D [0x01] GOTO 0x01AD
 60: 0x0170 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
 61: 0x0172 [0x02] IF !(Work_Zone[4] == 1*) GOTO 0x0186
 62: 0x017A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=36.082*, z=-40.352*, y=7.000*, direction=165.9°*
 63: 0x0183 [0x01] GOTO 0x01AB
 64: 0x0186 [0x02] IF !(Work_Zone[4] == 4*) GOTO 0x019A
 65: 0x018E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-185.276*, z=108.531*, y=-0.200*, direction=208.2°*
 66: 0x0197 [0x01] GOTO 0x01AB
 67: 0x019A [0x02] IF !(Work_Zone[4] == 5*) GOTO 0x01AB
 68: 0x01A2 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=28.607*, z=58.557*, y=-16.325*, direction=85.6°*

SUBROUTINE_01AB:
 69: 0x01AB [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)

SUBROUTINE_01AD:
 70: 0x01AD [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01AE   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                                            37 19                7.
01B0: 80 1A 80 1B 80 1C 80 00                           ........        
```

#### Opcodes

```
  0: 0x01AE [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=23.670*, z=32.388*, y=-18.274*, direction=128.2°*
  1: 0x01B7 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x01B8    |
| Data Size    | 119 bytes |
| Instructions | 21        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                          6C F8 FF FF 7F 1D 80 01          l.......
01C0: 80 1C 01 80 33 01 37 1E  80 1F 80 20 80 21 80 33  ....3.7.... .!.3
01D0: 01 1E F0 FF FF 7F 6C F8  FF FF 7F 22 80 23 80 1C  ......l....".#..
01E0: 24 80 6C F8 FF FF 7F 25  80 22 80 1C 22 80 37 26  $.l....%."..".7&
01F0: 80 27 80 28 80 29 80 1E  F0 FF FF 7F 6C F8 FF FF  .'.(.)......l...
0200: 7F 22 80 22 80 1C 23 80  6C F8 FF FF 7F 25 80 22  ."."..#.l....%."
0210: 80 1C 22 80 37 2A 80 2B  80 2C 80 2D 80 1E F0 FF  ..".7*.+.,.-....
0220: FF 7F 6C F8 FF FF 7F 22  80 22 80 1C 23 80 00     ..l...."."..#.. 
```

#### Opcodes

```
  0: 0x01B8 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=50*, fade_time=1*)
  1: 0x01C1 [0x1C] WAIT(1* ticks)
  2: 0x01C4 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  3: 0x01C6 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=23.058*, z=31.358*, y=-19.206*, direction=136.8°*
  4: 0x01CF [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  5: 0x01D1 [0x1E] EventEntity looks at LocalPlayer and starts talking
  6: 0x01D6 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=100*, fade_time=200*)
  7: 0x01DF [0x1C] WAIT(300* ticks)
  8: 0x01E2 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=100*)
  9: 0x01EB [0x1C] WAIT(100* ticks)
 10: 0x01EE [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=23.547*, z=29.391*, y=-19.241*, direction=258.9°*
 11: 0x01F7 [0x1E] EventEntity looks at LocalPlayer and starts talking
 12: 0x01FC [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=100*, fade_time=100*)
 13: 0x0205 [0x1C] WAIT(200* ticks)
 14: 0x0208 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=100*)
 15: 0x0211 [0x1C] WAIT(100* ticks)
 16: 0x0214 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=24.857*, z=30.831*, y=-18.308*, direction=129.4°*
 17: 0x021D [0x1E] EventEntity looks at LocalPlayer and starts talking
 18: 0x0222 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=100*, fade_time=100*)
 19: 0x022B [0x1C] WAIT(200* ticks)
 20: 0x022E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x022F   |
| Data Size    | 75 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:                                               6C                 l
0230: F8 FF FF 7F 22 80 01 80  1C 2E 80 03 00 00 01 80  ...."...........
0240: 02 00 00 01 80 00 79 02  1C 01 80 6C F8 FF FF 7F  ......y....l....
0250: 1D 80 22 80 02 00 00 01  80 00 5F 02 1C 2F 80 6C  .."......._../.l
0260: F8 FF FF 7F 22 80 22 80  1C 01 80 02 00 00 01 80  ....".".........
0270: 00 76 02 1C 2F 80 01 40  02 00                    .v../..@..      
```

#### Opcodes

```
  0: 0x022F [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=100*, fade_time=1*)
  1: 0x0238 [0x1C] WAIT(10* ticks)
  2: 0x023B [0x03] ExtData[1]->WorkLocal[0] = 1*
  3: 0x0240 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x0279
  4: 0x0248 [0x1C] WAIT(1* ticks)
  5: 0x024B [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=50*, fade_time=100*)
  6: 0x0254 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x025F
  7: 0x025C [0x1C] WAIT(150* ticks)
  8: 0x025F [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=100*, fade_time=100*)
  9: 0x0268 [0x1C] WAIT(1* ticks)
 10: 0x026B [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x0276
 11: 0x0273 [0x1C] WAIT(150* ticks)
 12: 0x0276 [0x01] GOTO 0x0240
 13: 0x0279 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x027A  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0270:                                03 00 00 25 80 00            ...%..
```

#### Opcodes

```
  0: 0x027A [0x03] ExtData[1]->WorkLocal[0] = 0*
  1: 0x027F [0x00] END_REQSTACK()
```
