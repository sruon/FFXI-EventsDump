# 17977519 - Disjoined One

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Reisenjima Sanctorium (ID: 293) |
| Block Size       | 892 bytes                       |
| Total Events     | 15                              |
| References Count | 21                              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     21 |              2 |
| [65535.2](#event-655352) | 0x0016       |    256 |             26 |
| [65535.3](#event-655353) | 0x0116       |    256 |             26 |
| [1](#event-1)            | 0x0216       |      1 |              1 |
| [2](#event-2)            | 0x0217       |      1 |              1 |
| [3](#event-3)            | 0x0218       |      4 |              2 |
| [65535.4](#event-655354) | 0x021C       |     10 |              2 |
| [4](#event-4)            | 0x0226       |      1 |              1 |
| [5](#event-5)            | 0x0227       |      1 |              1 |
| [65535.5](#event-655355) | 0x0228       |     10 |              2 |
| [65535.6](#event-655356) | 0x0232       |      7 |              3 |
| [65535.7](#event-655357) | 0x0239       |    155 |             35 |
| [65535.8](#event-655358) | 0x02D4       |      3 |              2 |
| [65535.9](#event-655359) | 0x02D7       |      3 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x0184      |         388 |
|       3 | 0x00E6      |         230 |
|       4 | 0x014A      |         330 |
|       5 | 0x00B9      |         185 |
|       6 | 0x0002      |           2 |
|       7 | 0x0003      |           3 |
|       8 | 0x0004      |           4 |
|       9 | 0x0005      |           5 |
|      10 | 0x0006      |           6 |
|      11 | 0x0007      |           7 |
|      12 | 0x0008      |           8 |
|      13 | 0x0080      |         128 |
|      14 | 0x003C      |          60 |
|      15 | 0x0042      |          66 |
|      16 | 0x000A      |          10 |
|      17 | 0x0009      |           9 |
|      18 | 0x0046      |          70 |
|      19 | 0x008C      |         140 |
|      20 | 0x00D2      |         210 |

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    B6 0B 00 80 01 80 02  80 03 80 03 80 03 80 03   ...............
0010: 80 01 80 01 80 00                                 ......          
```

#### Opcodes

```
  0: 0x0001 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=1*, hair=0*, head=388*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
  1: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0016    |
| Data Size    | 256 bytes |
| Instructions | 26        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   29 10  F0 FF FF 7F 02 02 02 10        ).........
0020: 00 80 80 3C 00 B6 0B 00  80 03 10 01 80 04 80 05  ...<............
0030: 80 03 80 03 80 01 80 01  80 01 15 01 02 02 10 06  ................
0040: 80 80 5B 00 B6 0B 06 80  03 10 01 80 04 80 05 80  ..[.............
0050: 03 80 03 80 01 80 01 80  01 15 01 02 02 10 07 80  ................
0060: 80 7A 00 B6 0B 07 80 03  10 01 80 04 80 05 80 03  .z..............
0070: 80 03 80 01 80 01 80 01  15 01 02 02 10 08 80 80  ................
0080: 99 00 B6 0B 08 80 03 10  01 80 04 80 05 80 03 80  ................
0090: 03 80 01 80 01 80 01 15  01 02 02 10 09 80 80 B8  ................
00A0: 00 B6 0B 09 80 03 10 01  80 04 80 05 80 03 80 03  ................
00B0: 80 01 80 01 80 01 15 01  02 02 10 0A 80 80 D7 00  ................
00C0: B6 0B 0A 80 03 10 01 80  04 80 05 80 03 80 03 80  ................
00D0: 01 80 01 80 01 15 01 02  02 10 0B 80 80 F6 00 B6  ................
00E0: 0B 0B 80 03 10 01 80 04  80 05 80 03 80 03 80 01  ................
00F0: 80 01 80 01 15 01 02 02  10 0C 80 80 15 01 B6 0B  ................
0100: 0C 80 03 10 01 80 04 80  05 80 03 80 03 80 01 80  ................
0110: 01 80 01 15 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0016 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x02)
  1: 0x001D [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x003C
  2: 0x0025 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=1*, hair=Work_Zone[3], head=0*, body=330*, hands=185*, legs=230*, feet=230*, main=0*, sub=0*)
  3: 0x0039 [0x01] GOTO 0x0115
  4: 0x003C [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x005B
  5: 0x0044 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=2*, hair=Work_Zone[3], head=0*, body=330*, hands=185*, legs=230*, feet=230*, main=0*, sub=0*)
  6: 0x0058 [0x01] GOTO 0x0115
  7: 0x005B [0x02] IF !(Work_Zone[2] == 3*) GOTO 0x007A
  8: 0x0063 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=Work_Zone[3], head=0*, body=330*, hands=185*, legs=230*, feet=230*, main=0*, sub=0*)
  9: 0x0077 [0x01] GOTO 0x0115
 10: 0x007A [0x02] IF !(Work_Zone[2] == 4*) GOTO 0x0099
 11: 0x0082 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=4*, hair=Work_Zone[3], head=0*, body=330*, hands=185*, legs=230*, feet=230*, main=0*, sub=0*)
 12: 0x0096 [0x01] GOTO 0x0115
 13: 0x0099 [0x02] IF !(Work_Zone[2] == 5*) GOTO 0x00B8
 14: 0x00A1 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=5*, hair=Work_Zone[3], head=0*, body=330*, hands=185*, legs=230*, feet=230*, main=0*, sub=0*)
 15: 0x00B5 [0x01] GOTO 0x0115
 16: 0x00B8 [0x02] IF !(Work_Zone[2] == 6*) GOTO 0x00D7
 17: 0x00C0 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=6*, hair=Work_Zone[3], head=0*, body=330*, hands=185*, legs=230*, feet=230*, main=0*, sub=0*)
 18: 0x00D4 [0x01] GOTO 0x0115
 19: 0x00D7 [0x02] IF !(Work_Zone[2] == 7*) GOTO 0x00F6
 20: 0x00DF [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=Work_Zone[3], head=0*, body=330*, hands=185*, legs=230*, feet=230*, main=0*, sub=0*)
 21: 0x00F3 [0x01] GOTO 0x0115
 22: 0x00F6 [0x02] IF !(Work_Zone[2] == 8*) GOTO 0x0115
 23: 0x00FE [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=8*, hair=Work_Zone[3], head=0*, body=330*, hands=185*, legs=230*, feet=230*, main=0*, sub=0*)
 24: 0x0112 [0x01] GOTO 0x0115

SUBROUTINE_0115:
 25: 0x0115 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0116    |
| Data Size    | 256 bytes |
| Instructions | 26        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                   29 10  F0 FF FF 7F 02 02 02 10        ).........
0120: 00 80 80 3C 01 B6 0B 00  80 03 10 02 80 04 10 05  ...<............
0130: 10 06 10 07 10 01 80 01  80 01 15 02 02 02 10 06  ................
0140: 80 80 5B 01 B6 0B 06 80  03 10 02 80 04 10 05 10  ..[.............
0150: 06 10 07 10 01 80 01 80  01 15 02 02 02 10 07 80  ................
0160: 80 7A 01 B6 0B 07 80 03  10 02 80 04 10 05 10 06  .z..............
0170: 10 07 10 01 80 01 80 01  15 02 02 02 10 08 80 80  ................
0180: 99 01 B6 0B 08 80 03 10  02 80 04 10 05 10 06 10  ................
0190: 07 10 01 80 01 80 01 15  02 02 02 10 09 80 80 B8  ................
01A0: 01 B6 0B 09 80 03 10 02  80 04 10 05 10 06 10 07  ................
01B0: 10 01 80 01 80 01 15 02  02 02 10 0A 80 80 D7 01  ................
01C0: B6 0B 0A 80 03 10 02 80  04 10 05 10 06 10 07 10  ................
01D0: 01 80 01 80 01 15 02 02  02 10 0B 80 80 F6 01 B6  ................
01E0: 0B 0B 80 03 10 02 80 04  10 05 10 06 10 07 10 01  ................
01F0: 80 01 80 01 15 02 02 02  10 0C 80 80 15 02 B6 0B  ................
0200: 0C 80 03 10 02 80 04 10  05 10 06 10 07 10 01 80  ................
0210: 01 80 01 15 02 00                                 ......          
```

#### Opcodes

```
  0: 0x0116 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x02)
  1: 0x011D [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x013C
  2: 0x0125 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=1*, hair=Work_Zone[3], head=388*, body=Work_Zone[4], hands=Work_Zone[5], legs=Work_Zone[6], feet=Work_Zone[7], main=0*, sub=0*)
  3: 0x0139 [0x01] GOTO 0x0215
  4: 0x013C [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x015B
  5: 0x0144 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=2*, hair=Work_Zone[3], head=388*, body=Work_Zone[4], hands=Work_Zone[5], legs=Work_Zone[6], feet=Work_Zone[7], main=0*, sub=0*)
  6: 0x0158 [0x01] GOTO 0x0215
  7: 0x015B [0x02] IF !(Work_Zone[2] == 3*) GOTO 0x017A
  8: 0x0163 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=Work_Zone[3], head=388*, body=Work_Zone[4], hands=Work_Zone[5], legs=Work_Zone[6], feet=Work_Zone[7], main=0*, sub=0*)
  9: 0x0177 [0x01] GOTO 0x0215
 10: 0x017A [0x02] IF !(Work_Zone[2] == 4*) GOTO 0x0199
 11: 0x0182 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=4*, hair=Work_Zone[3], head=388*, body=Work_Zone[4], hands=Work_Zone[5], legs=Work_Zone[6], feet=Work_Zone[7], main=0*, sub=0*)
 12: 0x0196 [0x01] GOTO 0x0215
 13: 0x0199 [0x02] IF !(Work_Zone[2] == 5*) GOTO 0x01B8
 14: 0x01A1 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=5*, hair=Work_Zone[3], head=388*, body=Work_Zone[4], hands=Work_Zone[5], legs=Work_Zone[6], feet=Work_Zone[7], main=0*, sub=0*)
 15: 0x01B5 [0x01] GOTO 0x0215
 16: 0x01B8 [0x02] IF !(Work_Zone[2] == 6*) GOTO 0x01D7
 17: 0x01C0 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=6*, hair=Work_Zone[3], head=388*, body=Work_Zone[4], hands=Work_Zone[5], legs=Work_Zone[6], feet=Work_Zone[7], main=0*, sub=0*)
 18: 0x01D4 [0x01] GOTO 0x0215
 19: 0x01D7 [0x02] IF !(Work_Zone[2] == 7*) GOTO 0x01F6
 20: 0x01DF [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=Work_Zone[3], head=388*, body=Work_Zone[4], hands=Work_Zone[5], legs=Work_Zone[6], feet=Work_Zone[7], main=0*, sub=0*)
 21: 0x01F3 [0x01] GOTO 0x0215
 22: 0x01F6 [0x02] IF !(Work_Zone[2] == 8*) GOTO 0x0215
 23: 0x01FE [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=8*, hair=Work_Zone[3], head=388*, body=Work_Zone[4], hands=Work_Zone[5], legs=Work_Zone[6], feet=Work_Zone[7], main=0*, sub=0*)
 24: 0x0212 [0x01] GOTO 0x0215

SUBROUTINE_0215:
 25: 0x0215 [0x00] END_REQSTACK()
```

### Event 1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0216  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0210:                   00                                    .         
```

#### Opcodes

```
  0: 0x0216 [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0217  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0210:                      00                                  .        
```

#### Opcodes

```
  0: 0x0217 [0x00] END_REQSTACK()
```

### Event 3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0218  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0210:                          C0 00 80 00                      ....    
```

#### Opcodes

```
  0: 0x0218 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x021B [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x021C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0210:                                      6C F8 FF FF              l...
0220: 7F 0D 80 00 80 00                                 ......          
```

#### Opcodes

```
  0: 0x021C [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0225 [0x00] END_REQSTACK()
```

### Event 4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0226  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:                   00                                    .         
```

#### Opcodes

```
  0: 0x0226 [0x00] END_REQSTACK()
```

### Event 5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0227  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:                      00                                  .        
```

#### Opcodes

```
  0: 0x0227 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0228   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:                          6C F8 FF FF 7F 01 80 0E          l.......
0230: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0228 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=60*)
  1: 0x0231 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0232  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0230:       AB 03 AC 01 0F 80  00                         .......       
```

#### Opcodes

```
  0: 0x0232 [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
  1: 0x0234 [0xAC] EventEntity->StatusEvent = 66*
  2: 0x0238 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0239    |
| Data Size    | 155 bytes |
| Instructions | 3         |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0230:                             AC 01 01 80 AB 04 00           .......
0240: 03 01 00 00 00 02 01 00  09 80 05 55 02 08 01 00  ...........U....
0250: 00 80 01 5A 02 08 01 00  06 80 14 01 00 10 80 07  ...Z............
0260: 01 00 11 80 1B 03 01 00  00 00 02 01 00 09 80 05  ................
0270: 7A 02 08 01 00 00 80 01  7F 02 08 01 00 06 80 14  z...............
0280: 01 00 10 80 07 01 00 12  80 1B 03 01 00 00 00 02  ................
0290: 01 00 09 80 05 9F 02 08  01 00 00 80 01 A4 02 08  ................
02A0: 01 00 06 80 14 01 00 10  80 07 01 00 13 80 1B 03  ................
02B0: 01 00 00 00 02 01 00 09  80 05 C4 02 08 01 00 00  ................
02C0: 80 01 C9 02 08 01 00 06  80 14 01 00 10 80 07 01  ................
02D0: 00 14 80 1B                                       ....            
```

#### Opcodes

```
  0: 0x0239 [0xAC] EventEntity->StatusEvent = 0*
  1: 0x023D [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  2: 0x023F [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0240 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x0245 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x0255
     0x024D [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0252 [0x01] GOTO 0x025A
     0x0255 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x025A [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x025F [0x07] ExtData[1]->WorkLocal[1] += 9*
     0x0264 [0x1B] RETURN
     0x0265 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x026A [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x027A
     0x0272 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x0277 [0x01] GOTO 0x027F
     0x027A [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x027F [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x0284 [0x07] ExtData[1]->WorkLocal[1] += 70*
     0x0289 [0x1B] RETURN
     0x028A [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x028F [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x029F
     0x0297 [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x029C [0x01] GOTO 0x02A4
     0x029F [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x02A4 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x02A9 [0x07] ExtData[1]->WorkLocal[1] += 140*
     0x02AE [0x1B] RETURN
     0x02AF [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->WorkLocal[0]
     0x02B4 [0x02] IF !(ExtData[1]->WorkLocal[1] > 5*) GOTO 0x02C4
     0x02BC [0x08] ExtData[1]->WorkLocal[1] -= 1*
     0x02C1 [0x01] GOTO 0x02C9
     0x02C4 [0x08] ExtData[1]->WorkLocal[1] -= 2*
     0x02C9 [0x14] ExtData[1]->WorkLocal[1] *= 10*
     0x02CE [0x07] ExtData[1]->WorkLocal[1] += 210*
     0x02D3 [0x1B] RETURN
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x02D4  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02D0:             61 01 00                                  a..         
```

#### Opcodes

```
  0: 0x02D4 [0x61] EventEntity->Render.Flags2 |= 0x00000001
  1: 0x02D6 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x02D7  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02D0:                      61  00 00                           a..      
```

#### Opcodes

```
  0: 0x02D7 [0x61] EventEntity->Render.Flags2 &= ~0x00000001
  1: 0x02D9 [0x00] END_REQSTACK()
```
