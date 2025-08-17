# 17788979 - Talking Doll

## Common Data

| Field            | Value           |
|------------------|-----------------|
| Zone             | Rabao (ID: 247) |
| Block Size       | 1004 bytes      |
| Total Events     | 11              |
| References Count | 62              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [69](#event-69)          | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |    422 |             71 |
| [65535.2](#event-655352) | 0x01AE       |     10 |              2 |
| [65535.3](#event-655353) | 0x01B8       |    119 |             21 |
| [65535.4](#event-655354) | 0x022F       |     75 |             14 |
| [65535.5](#event-655355) | 0x027A       |      6 |              2 |
| [187](#event-187)        | 0x0280       |      7 |              2 |
| [65535.6](#event-655356) | 0x0287       |     16 |              2 |
| [65535.7](#event-655357) | 0x0297       |     22 |              4 |
| [65535.8](#event-655358) | 0x02AD       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0003      |           3 |
|       1 | 0x0000      |           0 |
|       2 | 0x17C6A     |       97386 |
|       3 | 0xFFFE8198  |  4294869400 |
|       4 | 0xFFFFC569  |  4294952297 |
|       5 | 0x0FC6      |        4038 |
|       6 | 0x0002      |           2 |
|       7 | 0xFFFFC8EC  |  4294953196 |
|       8 | 0xFFFFAB9A  |  4294945690 |
|       9 | 0x012C      |         300 |
|      10 | 0x0FC1      |        4033 |
|      11 | 0xFFFFB5F6  |  4294948342 |
|      12 | 0xFFFFCF44  |  4294954820 |
|      13 | 0x1B58      |        7000 |
|      14 | 0x0004      |           4 |
|      15 | 0x0005      |           5 |
|      16 | 0x17C20     |       97312 |
|      17 | 0xFFFE82A8  |  4294869672 |
|      18 | 0xFFFFCC0C  |  4294953996 |
|      19 | 0x0FBB      |        4027 |
|      20 | 0xFFFFC7ED  |  4294952941 |
|      21 | 0xFFFFACA2  |  4294945954 |
|      22 | 0x0511      |        1297 |
|      23 | 0x0F56      |        3926 |
|      24 | 0xFFFFB4FC  |  4294948092 |
|      25 | 0xFFFFD018  |  4294955032 |
|      26 | 0x1F40      |        8000 |
|      27 | 0x0FE9      |        4073 |
|      28 | 0x0006      |           6 |
|      29 | 0x0008      |           8 |
|      30 | 0x0E10      |        3600 |
|      31 | 0xFFFFC824  |  4294952996 |
|      32 | 0x01F4      |         500 |
|      33 | 0xFFFFB89F  |  4294949023 |
|      34 | 0xFFFFD02F  |  4294955055 |
|      35 | 0x1C20      |        7200 |
|      36 | 0x0F39      |        3897 |
|      37 | 0x5C76      |       23670 |
|      38 | 0x7E84      |       32388 |
|      39 | 0xFFFFB89E  |  4294949022 |
|      40 | 0x05B3      |        1459 |
|      41 | 0x0032      |          50 |
|      42 | 0x0001      |           1 |
|      43 | 0x5A12      |       23058 |
|      44 | 0x7A7E      |       31358 |
|      45 | 0xFFFFB4FA  |  4294948090 |
|      46 | 0x0615      |        1557 |
|      47 | 0x0064      |         100 |
|      48 | 0x00C8      |         200 |
|      49 | 0x5BFB      |       23547 |
|      50 | 0x72CF      |       29391 |
|      51 | 0xFFFFB4D7  |  4294948055 |
|      52 | 0x0B82      |        2946 |
|      53 | 0x6119      |       24857 |
|      54 | 0x786F      |       30831 |
|      55 | 0xFFFFB87C  |  4294948988 |
|      56 | 0x05C0      |        1472 |
|      57 | 0x000A      |          10 |
|      58 | 0x0096      |         150 |
|      59 | 0x00FC      |         252 |
|      60 | 0x001E      |          30 |
|      61 | 0x0080      |         128 |

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

### Event 69

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
0030: 80 08 80 09 80 0A 80 01  4B 00 02 04 10 00 80 00  ........K.......
0040: 4B 00 37 0B 80 0C 80 0D  80 01 80 33 01 01 AD 01  K.7........3....
0050: 02 09 10 0E 80 80 98 00  33 01 02 04 10 01 80 00  ........3.......
0060: 6E 00 37 02 80 03 80 04  80 05 80 01 93 00 02 04  n.7.............
0070: 10 06 80 00 82 00 37 07  80 08 80 09 80 0A 80 01  ......7.........
0080: 93 00 02 04 10 00 80 00  93 00 37 0B 80 0C 80 0D  ..........7.....
0090: 80 01 80 33 01 01 AD 01  02 09 10 0F 80 80 E0 00  ...3............
00A0: 33 01 02 04 10 01 80 00  B6 00 37 10 80 11 80 12  3.........7.....
00B0: 80 13 80 01 DB 00 02 04  10 06 80 00 CA 00 37 14  ..............7.
00C0: 80 15 80 16 80 17 80 01  DB 00 02 04 10 00 80 00  ................
00D0: DB 00 37 18 80 19 80 1A  80 1B 80 33 01 01 AD 01  ..7........3....
00E0: 02 09 10 1C 80 80 28 01  33 01 02 04 10 01 80 00  ......(.3.......
00F0: FE 00 37 10 80 11 80 12  80 13 80 01 23 01 02 04  ..7.........#...
0100: 10 06 80 00 12 01 37 14  80 15 80 16 80 17 80 01  ......7.........
0110: 23 01 02 04 10 00 80 00  23 01 37 18 80 19 80 1A  #.......#.7.....
0120: 80 1B 80 33 01 01 AD 01  02 09 10 1D 80 80 70 01  ...3..........p.
0130: 33 01 02 04 10 01 80 00  46 01 37 02 80 03 80 04  3.......F.7.....
0140: 80 05 80 01 6B 01 02 04  10 06 80 00 5A 01 37 07  ....k.......Z.7.
0150: 80 08 80 09 80 1E 80 01  6B 01 02 04 10 00 80 00  ........k.......
0160: 6B 01 37 0B 80 0C 80 0D  80 01 80 33 01 01 AD 01  k.7........3....
0170: 33 01 02 04 10 01 80 00  86 01 37 02 80 03 80 1F  3.........7.....
0180: 80 05 80 01 AB 01 02 04  10 06 80 00 9A 01 37 07  ..............7.
0190: 80 08 80 20 80 1E 80 01  AB 01 02 04 10 00 80 00  ... ............
01A0: AB 01 37 21 80 22 80 23  80 24 80 33 01 00        ..7!.".#.$.3..  
```

#### Opcodes

```
  0: 0x0008 [0x02] IF !(Work_Zone[9] == 3*) GOTO 0x0050
  1: 0x0010 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  2: 0x0012 [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x0026
  3: 0x001A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=97.386*, z=-97.896*, y=-14.999*, direction=354.9°*
  4: 0x0023 [0x01] GOTO 0x004B
  5: 0x0026 [0x02] IF !(Work_Zone[4] == 2*) GOTO 0x003A
  6: 0x002E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-14.100*, z=-21.606*, y=0.300*, direction=354.5°*
  7: 0x0037 [0x01] GOTO 0x004B
  8: 0x003A [0x02] IF !(Work_Zone[4] == 3*) GOTO 0x004B
  9: 0x0042 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-18.954*, z=-12.476*, y=7.000*, direction=0.0°*

SUBROUTINE_004B:
 10: 0x004B [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
 11: 0x004D [0x01] GOTO 0x01AD
 12: 0x0050 [0x02] IF !(Work_Zone[9] == 4*) GOTO 0x0098
 13: 0x0058 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
 14: 0x005A [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x006E
 15: 0x0062 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=97.386*, z=-97.896*, y=-14.999*, direction=354.9°*
 16: 0x006B [0x01] GOTO 0x0093
 17: 0x006E [0x02] IF !(Work_Zone[4] == 2*) GOTO 0x0082
 18: 0x0076 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-14.100*, z=-21.606*, y=0.300*, direction=354.5°*
 19: 0x007F [0x01] GOTO 0x0093
 20: 0x0082 [0x02] IF !(Work_Zone[4] == 3*) GOTO 0x0093
 21: 0x008A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-18.954*, z=-12.476*, y=7.000*, direction=0.0°*

SUBROUTINE_0093:
 22: 0x0093 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
 23: 0x0095 [0x01] GOTO 0x01AD
 24: 0x0098 [0x02] IF !(Work_Zone[9] == 5*) GOTO 0x00E0
 25: 0x00A0 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
 26: 0x00A2 [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x00B6
 27: 0x00AA [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=97.312*, z=-97.624*, y=-13.300*, direction=353.9°*
 28: 0x00B3 [0x01] GOTO 0x00DB
 29: 0x00B6 [0x02] IF !(Work_Zone[4] == 2*) GOTO 0x00CA
 30: 0x00BE [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-14.355*, z=-21.342*, y=1.297*, direction=345.0°*
 31: 0x00C7 [0x01] GOTO 0x00DB
 32: 0x00CA [0x02] IF !(Work_Zone[4] == 3*) GOTO 0x00DB
 33: 0x00D2 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-19.204*, z=-12.264*, y=8.000*, direction=358.0°*

SUBROUTINE_00DB:
 34: 0x00DB [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
 35: 0x00DD [0x01] GOTO 0x01AD
 36: 0x00E0 [0x02] IF !(Work_Zone[9] == 6*) GOTO 0x0128
 37: 0x00E8 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
 38: 0x00EA [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x00FE
 39: 0x00F2 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=97.312*, z=-97.624*, y=-13.300*, direction=353.9°*
 40: 0x00FB [0x01] GOTO 0x0123
 41: 0x00FE [0x02] IF !(Work_Zone[4] == 2*) GOTO 0x0112
 42: 0x0106 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-14.355*, z=-21.342*, y=1.297*, direction=345.0°*
 43: 0x010F [0x01] GOTO 0x0123
 44: 0x0112 [0x02] IF !(Work_Zone[4] == 3*) GOTO 0x0123
 45: 0x011A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-19.204*, z=-12.264*, y=8.000*, direction=358.0°*

SUBROUTINE_0123:
 46: 0x0123 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
 47: 0x0125 [0x01] GOTO 0x01AD
 48: 0x0128 [0x02] IF !(Work_Zone[9] == 8*) GOTO 0x0170
 49: 0x0130 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
 50: 0x0132 [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x0146
 51: 0x013A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=97.386*, z=-97.896*, y=-14.999*, direction=354.9°*
 52: 0x0143 [0x01] GOTO 0x016B
 53: 0x0146 [0x02] IF !(Work_Zone[4] == 2*) GOTO 0x015A
 54: 0x014E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-14.100*, z=-21.606*, y=0.300*, direction=316.4°*
 55: 0x0157 [0x01] GOTO 0x016B
 56: 0x015A [0x02] IF !(Work_Zone[4] == 3*) GOTO 0x016B
 57: 0x0162 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-18.954*, z=-12.476*, y=7.000*, direction=0.0°*

SUBROUTINE_016B:
 58: 0x016B [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
 59: 0x016D [0x01] GOTO 0x01AD
 60: 0x0170 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
 61: 0x0172 [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x0186
 62: 0x017A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=97.386*, z=-97.896*, y=-14.300*, direction=354.9°*
 63: 0x0183 [0x01] GOTO 0x01AB
 64: 0x0186 [0x02] IF !(Work_Zone[4] == 2*) GOTO 0x019A
 65: 0x018E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-14.100*, z=-21.606*, y=0.500*, direction=316.4°*
 66: 0x0197 [0x01] GOTO 0x01AB
 67: 0x019A [0x02] IF !(Work_Zone[4] == 3*) GOTO 0x01AB
 68: 0x01A2 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-18.273*, z=-12.241*, y=7.200*, direction=342.5°*

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
01A0:                                            37 25                7%
01B0: 80 26 80 27 80 28 80 00                           .&.'.(..        
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
01B0:                          6C F8 FF FF 7F 29 80 2A          l....).*
01C0: 80 1C 2A 80 33 01 37 2B  80 2C 80 2D 80 2E 80 33  ..*.3.7+.,.-...3
01D0: 01 1E F0 FF FF 7F 6C F8  FF FF 7F 2F 80 30 80 1C  ......l..../.0..
01E0: 09 80 6C F8 FF FF 7F 01  80 2F 80 1C 2F 80 37 31  ..l....../../.71
01F0: 80 32 80 33 80 34 80 1E  F0 FF FF 7F 6C F8 FF FF  .2.3.4......l...
0200: 7F 2F 80 2F 80 1C 30 80  6C F8 FF FF 7F 01 80 2F  ././..0.l....../
0210: 80 1C 2F 80 37 35 80 36  80 37 80 38 80 1E F0 FF  ../.75.6.7.8....
0220: FF 7F 6C F8 FF FF 7F 2F  80 2F 80 1C 30 80 00     ..l...././..0.. 
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
0230: F8 FF FF 7F 2F 80 2A 80  1C 39 80 03 00 00 2A 80  ..../.*..9....*.
0240: 02 00 00 2A 80 00 79 02  1C 2A 80 6C F8 FF FF 7F  ...*..y..*.l....
0250: 29 80 2F 80 02 00 00 2A  80 00 5F 02 1C 3A 80 6C  )./....*.._..:.l
0260: F8 FF FF 7F 2F 80 2F 80  1C 2A 80 02 00 00 2A 80  ...././..*....*.
0270: 00 76 02 1C 3A 80 01 40  02 00                    .v..:..@..      
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
0270:                                03 00 00 01 80 00            ......
```

#### Opcodes

```
  0: 0x027A [0x03] ExtData[1]->WorkLocal[0] = 0*
  1: 0x027F [0x00] END_REQSTACK()
```

### Event 187

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0280  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0280: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0280 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0286 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0287   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0280:                      5B  3B 80 F8 FF FF 7F F8 FF         [;.......
0290: FF 7F 62 72 75 30 00                              ..bru0.         
```

#### Opcodes

```
  0: 0x0287 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bru0" with entities [EventEntity, EventEntity], work=252*
  1: 0x0296 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0297   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0290:                      53  F8 FF FF 7F F8 FF FF 7F         S........
02A0: 62 72 75 30 5E 69 64 6C  30 1C 3C 80 00           bru0^idl0.<..   
```

#### Opcodes

```
  0: 0x0297 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "bru0" with entities [EventEntity, EventEntity]
  1: 0x02A4 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x02A9 [0x1C] WAIT(30* ticks)
  3: 0x02AC [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02AD   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02A0:                                         6C 33 70               l3p
02B0: 0F 01 3D 80 39 80 00                              ..=.9..         
```

#### Opcodes

```
  0: 0x02AD [0x6C] FADE_ENTITY_COLOR(entity_id=Talking Doll (ID: 17788979/0x010F7033), end_alpha=128*, fade_time=10*)
  1: 0x02B6 [0x00] END_REQSTACK()
```
