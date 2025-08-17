# 16924803 - Volto Oscuro

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Empyreal Paradox (ID: 36) |
| Block Size       | 1172 bytes                |
| Total Events     | 22                        |
| References Count | 16                        |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [9](#event-9)              | 0x0001       |      1 |              1 |
| [10](#event-10)            | 0x0002       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0003       |     43 |              6 |
| [65535.2](#event-655352)   | 0x002E       |     10 |              2 |
| [65535.3](#event-655353)   | 0x0038       |    256 |             26 |
| [65535.4](#event-655354)   | 0x0138       |     21 |              2 |
| [65535.5](#event-655355)   | 0x014D       |     10 |              2 |
| [65535.6](#event-655356)   | 0x0157       |      3 |              2 |
| [65535.7](#event-655357)   | 0x015A       |     21 |              2 |
| [65535.8](#event-655358)   | 0x016F       |     21 |              2 |
| [11](#event-11)            | 0x0184       |      1 |              1 |
| [12](#event-12)            | 0x0185       |      1 |              1 |
| [65535.9](#event-655359)   | 0x0186       |    256 |             26 |
| [13](#event-13)            | 0x0286       |     21 |              2 |
| [65535.10](#event-6553510) | 0x029B       |     25 |              3 |
| [65535.11](#event-6553511) | 0x02B4       |     25 |              3 |
| [14](#event-14)            | 0x02CD       |      1 |              1 |
| [65535.12](#event-6553512) | 0x02CE       |    256 |             26 |
| [65535.13](#event-6553513) | 0x03CE       |     10 |              2 |
| [65535.14](#event-6553514) | 0x03D8       |     18 |              2 |
| [17](#event-17)            | 0x03EA       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x003C      |          60 |
|       2 | 0x0001      |           1 |
|       3 | 0x0184      |         388 |
|       4 | 0x00E6      |         230 |
|       5 | 0x0080      |         128 |
|       6 | 0x0002      |           2 |
|       7 | 0x0003      |           3 |
|       8 | 0x0004      |           4 |
|       9 | 0x0005      |           5 |
|      10 | 0x0006      |           6 |
|      11 | 0x0007      |           7 |
|      12 | 0x0008      |           8 |
|      13 | 0x0140      |         320 |
|      14 | 0x014A      |         330 |
|      15 | 0x00B9      |         185 |

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

### Event 9

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

### Event 10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 43 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          6C F8 FF FF 7F  00 80 01 80 22 01 B6 0B     l........"...
0010: 02 80 00 80 03 80 04 80  04 80 04 80 04 80 00 80  ................
0020: 00 80 6C F8 FF FF 7F 00  80 02 80 22 00 00        ..l........"..  
```

#### Opcodes

```
  0: 0x0003 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=60*)
  1: 0x000C [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  2: 0x000E [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=1*, hair=0*, head=388*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
  3: 0x0022 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  4: 0x002B [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  5: 0x002D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            6C F8                l.
0030: FF FF 7F 05 80 01 80 00                           ........        
```

#### Opcodes

```
  0: 0x002E [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=60*)
  1: 0x0037 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0038    |
| Data Size    | 256 bytes |
| Instructions | 26        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          29 10 F0 FF FF 7F 0D 02          ).......
0040: 02 10 02 80 80 5E 00 B6  0B 02 80 03 10 03 80 04  .....^..........
0050: 10 05 10 06 10 07 10 00  80 00 80 01 37 01 02 02  ............7...
0060: 10 06 80 80 7D 00 B6 0B  06 80 03 10 03 80 04 10  ....}...........
0070: 05 10 06 10 07 10 00 80  00 80 01 37 01 02 02 10  ...........7....
0080: 07 80 80 9C 00 B6 0B 07  80 03 10 03 80 04 10 05  ................
0090: 10 06 10 07 10 00 80 00  80 01 37 01 02 02 10 08  ..........7.....
00A0: 80 80 BB 00 B6 0B 08 80  03 10 03 80 04 10 05 10  ................
00B0: 06 10 07 10 00 80 00 80  01 37 01 02 02 10 09 80  .........7......
00C0: 80 DA 00 B6 0B 09 80 03  10 03 80 04 10 05 10 06  ................
00D0: 10 07 10 00 80 00 80 01  37 01 02 02 10 0A 80 80  ........7.......
00E0: F9 00 B6 0B 0A 80 03 10  03 80 04 10 05 10 06 10  ................
00F0: 07 10 00 80 00 80 01 37  01 02 02 10 0B 80 80 18  .......7........
0100: 01 B6 0B 0B 80 03 10 03  80 04 10 05 10 06 10 07  ................
0110: 10 00 80 00 80 01 37 01  02 02 10 0C 80 80 37 01  ......7.......7.
0120: B6 0B 0C 80 03 10 03 80  04 10 05 10 06 10 07 10  ................
0130: 00 80 00 80 01 37 01 00                           .....7..        
```

#### Opcodes

```
  0: 0x0038 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x0D)
  1: 0x003F [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x005E
  2: 0x0047 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=1*, hair=Work_Zone[3], head=388*, body=Work_Zone[4], hands=Work_Zone[5], legs=Work_Zone[6], feet=Work_Zone[7], main=0*, sub=0*)
  3: 0x005B [0x01] GOTO 0x0137
  4: 0x005E [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x007D
  5: 0x0066 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=2*, hair=Work_Zone[3], head=388*, body=Work_Zone[4], hands=Work_Zone[5], legs=Work_Zone[6], feet=Work_Zone[7], main=0*, sub=0*)
  6: 0x007A [0x01] GOTO 0x0137
  7: 0x007D [0x02] IF !(Work_Zone[2] == 3*) GOTO 0x009C
  8: 0x0085 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=Work_Zone[3], head=388*, body=Work_Zone[4], hands=Work_Zone[5], legs=Work_Zone[6], feet=Work_Zone[7], main=0*, sub=0*)
  9: 0x0099 [0x01] GOTO 0x0137
 10: 0x009C [0x02] IF !(Work_Zone[2] == 4*) GOTO 0x00BB
 11: 0x00A4 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=4*, hair=Work_Zone[3], head=388*, body=Work_Zone[4], hands=Work_Zone[5], legs=Work_Zone[6], feet=Work_Zone[7], main=0*, sub=0*)
 12: 0x00B8 [0x01] GOTO 0x0137
 13: 0x00BB [0x02] IF !(Work_Zone[2] == 5*) GOTO 0x00DA
 14: 0x00C3 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=5*, hair=Work_Zone[3], head=388*, body=Work_Zone[4], hands=Work_Zone[5], legs=Work_Zone[6], feet=Work_Zone[7], main=0*, sub=0*)
 15: 0x00D7 [0x01] GOTO 0x0137
 16: 0x00DA [0x02] IF !(Work_Zone[2] == 6*) GOTO 0x00F9
 17: 0x00E2 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=6*, hair=Work_Zone[3], head=388*, body=Work_Zone[4], hands=Work_Zone[5], legs=Work_Zone[6], feet=Work_Zone[7], main=0*, sub=0*)
 18: 0x00F6 [0x01] GOTO 0x0137
 19: 0x00F9 [0x02] IF !(Work_Zone[2] == 7*) GOTO 0x0118
 20: 0x0101 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=Work_Zone[3], head=388*, body=Work_Zone[4], hands=Work_Zone[5], legs=Work_Zone[6], feet=Work_Zone[7], main=0*, sub=0*)
 21: 0x0115 [0x01] GOTO 0x0137
 22: 0x0118 [0x02] IF !(Work_Zone[2] == 8*) GOTO 0x0137
 23: 0x0120 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=8*, hair=Work_Zone[3], head=388*, body=Work_Zone[4], hands=Work_Zone[5], legs=Work_Zone[6], feet=Work_Zone[7], main=0*, sub=0*)
 24: 0x0134 [0x01] GOTO 0x0137

SUBROUTINE_0137:
 25: 0x0137 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0138   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                          B6 0B 02 80 00 80 03 80          ........
0140: 04 80 04 80 04 80 04 80  00 80 00 80 00           .............   
```

#### Opcodes

```
  0: 0x0138 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=1*, hair=0*, head=388*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
  1: 0x014C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                         6C F8 FF               l..
0150: FF 7F 00 80 02 80 00                              .......         
```

#### Opcodes

```
  0: 0x014D [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0156 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0157  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                      A4  01 00                           ...      
```

#### Opcodes

```
  0: 0x0157 [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  1: 0x0159 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015A   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                B6 0B 02 80 00 80            ......
0160: 03 80 04 80 04 80 04 80  04 80 0D 80 00 80 00     ............... 
```

#### Opcodes

```
  0: 0x015A [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=1*, hair=0*, head=388*, body=230*, hands=230*, legs=230*, feet=230*, main=320*, sub=0*)
  1: 0x016E [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x016F   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                               B6                 .
0170: 0B 0C 80 0A 80 03 80 04  80 04 80 04 80 04 80 00  ................
0180: 80 00 80 00                                       ....            
```

#### Opcodes

```
  0: 0x016F [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=8*, hair=6*, head=388*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
  1: 0x0183 [0x00] END_REQSTACK()
```

### Event 11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0184  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:             00                                        .           
```

#### Opcodes

```
  0: 0x0184 [0x00] END_REQSTACK()
```

### Event 12

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0185  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                00                                      .          
```

#### Opcodes

```
  0: 0x0185 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0186    |
| Data Size    | 256 bytes |
| Instructions | 26        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                   29 10  F0 FF FF 7F 0D 02 02 10        ).........
0190: 02 80 80 AC 01 B6 0B 02  80 03 10 00 80 0E 80 0F  ................
01A0: 80 04 80 04 80 00 80 00  80 01 85 02 02 02 10 06  ................
01B0: 80 80 CB 01 B6 0B 06 80  03 10 00 80 0E 80 0F 80  ................
01C0: 04 80 04 80 00 80 00 80  01 85 02 02 02 10 07 80  ................
01D0: 80 EA 01 B6 0B 07 80 03  10 00 80 0E 80 0F 80 04  ................
01E0: 80 04 80 00 80 00 80 01  85 02 02 02 10 08 80 80  ................
01F0: 09 02 B6 0B 08 80 03 10  00 80 0E 80 0F 80 04 80  ................
0200: 04 80 00 80 00 80 01 85  02 02 02 10 09 80 80 28  ...............(
0210: 02 B6 0B 09 80 03 10 00  80 0E 80 0F 80 04 80 04  ................
0220: 80 00 80 00 80 01 85 02  02 02 10 0A 80 80 47 02  ..............G.
0230: B6 0B 0A 80 03 10 00 80  0E 80 0F 80 04 80 04 80  ................
0240: 00 80 00 80 01 85 02 02  02 10 0B 80 80 66 02 B6  .............f..
0250: 0B 0B 80 03 10 00 80 0E  80 0F 80 04 80 04 80 00  ................
0260: 80 00 80 01 85 02 02 02  10 0C 80 80 85 02 B6 0B  ................
0270: 0C 80 03 10 00 80 0E 80  0F 80 04 80 04 80 00 80  ................
0280: 00 80 01 85 02 00                                 ......          
```

#### Opcodes

```
  0: 0x0186 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x0D)
  1: 0x018D [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x01AC
  2: 0x0195 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=1*, hair=Work_Zone[3], head=0*, body=330*, hands=185*, legs=230*, feet=230*, main=0*, sub=0*)
  3: 0x01A9 [0x01] GOTO 0x0285
  4: 0x01AC [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x01CB
  5: 0x01B4 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=2*, hair=Work_Zone[3], head=0*, body=330*, hands=185*, legs=230*, feet=230*, main=0*, sub=0*)
  6: 0x01C8 [0x01] GOTO 0x0285
  7: 0x01CB [0x02] IF !(Work_Zone[2] == 3*) GOTO 0x01EA
  8: 0x01D3 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=Work_Zone[3], head=0*, body=330*, hands=185*, legs=230*, feet=230*, main=0*, sub=0*)
  9: 0x01E7 [0x01] GOTO 0x0285
 10: 0x01EA [0x02] IF !(Work_Zone[2] == 4*) GOTO 0x0209
 11: 0x01F2 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=4*, hair=Work_Zone[3], head=0*, body=330*, hands=185*, legs=230*, feet=230*, main=0*, sub=0*)
 12: 0x0206 [0x01] GOTO 0x0285
 13: 0x0209 [0x02] IF !(Work_Zone[2] == 5*) GOTO 0x0228
 14: 0x0211 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=5*, hair=Work_Zone[3], head=0*, body=330*, hands=185*, legs=230*, feet=230*, main=0*, sub=0*)
 15: 0x0225 [0x01] GOTO 0x0285
 16: 0x0228 [0x02] IF !(Work_Zone[2] == 6*) GOTO 0x0247
 17: 0x0230 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=6*, hair=Work_Zone[3], head=0*, body=330*, hands=185*, legs=230*, feet=230*, main=0*, sub=0*)
 18: 0x0244 [0x01] GOTO 0x0285
 19: 0x0247 [0x02] IF !(Work_Zone[2] == 7*) GOTO 0x0266
 20: 0x024F [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=Work_Zone[3], head=0*, body=330*, hands=185*, legs=230*, feet=230*, main=0*, sub=0*)
 21: 0x0263 [0x01] GOTO 0x0285
 22: 0x0266 [0x02] IF !(Work_Zone[2] == 8*) GOTO 0x0285
 23: 0x026E [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=8*, hair=Work_Zone[3], head=0*, body=330*, hands=185*, legs=230*, feet=230*, main=0*, sub=0*)
 24: 0x0282 [0x01] GOTO 0x0285

SUBROUTINE_0285:
 25: 0x0285 [0x00] END_REQSTACK()
```

### Event 13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0286   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0280:                   B6 0B  02 80 00 80 03 80 04 80        ..........
0290: 04 80 04 80 04 80 00 80  00 80 00                 ...........     
```

#### Opcodes

```
  0: 0x0286 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=1*, hair=0*, head=388*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
  1: 0x029A [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x029B   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0290:                                   B4 13 00 00 56             ....V
02A0: 6F 6C 74 6F 40 4F 73 63  75 72 6F 00 00 00 00 B5  olto@Oscuro.....
02B0: 00 00 00 00                                       ....            
```

#### Opcodes

```
  0: 0x029B [0xB4] UI_WINDOW_STRING_HANDLER(case=0x13 - Copy string and replace @ with space, work_offset=ExtData[1]->WorkLocal[0], string="Volto@Oscuro")
  1: 0x02AF [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x02B3 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02B4   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02B0:             B4 13 00 00  44 69 73 6A 6F 69 6E 65      ....Disjoine
02C0: 64 40 4F 6E 65 00 00 00  B5 00 00 00 00           d@One........   
```

#### Opcodes

```
  0: 0x02B4 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x13 - Copy string and replace @ with space, work_offset=ExtData[1]->WorkLocal[0], string="Disjoined@One")
  1: 0x02C8 [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x02CC [0x00] END_REQSTACK()
```

### Event 14

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x02CD  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02C0:                                         00                     .  
```

#### Opcodes

```
  0: 0x02CD [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x02CE    |
| Data Size    | 256 bytes |
| Instructions | 26        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02C0:                                            29 10                ).
02D0: F0 FF FF 7F 0D 02 02 10  02 80 80 F4 02 B6 0B 02  ................
02E0: 80 03 10 00 80 04 80 04  80 04 80 04 80 00 80 00  ................
02F0: 80 01 CD 03 02 02 10 06  80 80 13 03 B6 0B 06 80  ................
0300: 03 10 00 80 04 80 04 80  04 80 04 80 00 80 00 80  ................
0310: 01 CD 03 02 02 10 07 80  80 32 03 B6 0B 07 80 03  .........2......
0320: 10 00 80 04 80 04 80 04  80 04 80 00 80 00 80 01  ................
0330: CD 03 02 02 10 08 80 80  51 03 B6 0B 08 80 03 10  ........Q.......
0340: 00 80 04 80 04 80 04 80  04 80 00 80 00 80 01 CD  ................
0350: 03 02 02 10 09 80 80 70  03 B6 0B 09 80 03 10 00  .......p........
0360: 80 04 80 04 80 04 80 04  80 00 80 00 80 01 CD 03  ................
0370: 02 02 10 0A 80 80 8F 03  B6 0B 0A 80 03 10 00 80  ................
0380: 04 80 04 80 04 80 04 80  00 80 00 80 01 CD 03 02  ................
0390: 02 10 0B 80 80 AE 03 B6  0B 0B 80 03 10 00 80 04  ................
03A0: 80 04 80 04 80 04 80 00  80 00 80 01 CD 03 02 02  ................
03B0: 10 0C 80 80 CD 03 B6 0B  0C 80 03 10 00 80 04 80  ................
03C0: 04 80 04 80 04 80 00 80  00 80 01 CD 03 00        ..............  
```

#### Opcodes

```
  0: 0x02CE [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x0D)
  1: 0x02D5 [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x02F4
  2: 0x02DD [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=1*, hair=Work_Zone[3], head=0*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
  3: 0x02F1 [0x01] GOTO 0x03CD
  4: 0x02F4 [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x0313
  5: 0x02FC [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=2*, hair=Work_Zone[3], head=0*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
  6: 0x0310 [0x01] GOTO 0x03CD
  7: 0x0313 [0x02] IF !(Work_Zone[2] == 3*) GOTO 0x0332
  8: 0x031B [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=Work_Zone[3], head=0*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
  9: 0x032F [0x01] GOTO 0x03CD
 10: 0x0332 [0x02] IF !(Work_Zone[2] == 4*) GOTO 0x0351
 11: 0x033A [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=4*, hair=Work_Zone[3], head=0*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
 12: 0x034E [0x01] GOTO 0x03CD
 13: 0x0351 [0x02] IF !(Work_Zone[2] == 5*) GOTO 0x0370
 14: 0x0359 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=5*, hair=Work_Zone[3], head=0*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
 15: 0x036D [0x01] GOTO 0x03CD
 16: 0x0370 [0x02] IF !(Work_Zone[2] == 6*) GOTO 0x038F
 17: 0x0378 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=6*, hair=Work_Zone[3], head=0*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
 18: 0x038C [0x01] GOTO 0x03CD
 19: 0x038F [0x02] IF !(Work_Zone[2] == 7*) GOTO 0x03AE
 20: 0x0397 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=Work_Zone[3], head=0*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
 21: 0x03AB [0x01] GOTO 0x03CD
 22: 0x03AE [0x02] IF !(Work_Zone[2] == 8*) GOTO 0x03CD
 23: 0x03B6 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=8*, hair=Work_Zone[3], head=0*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
 24: 0x03CA [0x01] GOTO 0x03CD

SUBROUTINE_03CD:
 25: 0x03CD [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x03CE   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03C0:                                            6C F8                l.
03D0: FF FF 7F 00 80 01 80 00                           ........        
```

#### Opcodes

```
  0: 0x03CE [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=60*)
  1: 0x03D7 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x03D8   |
| Data Size    | 18 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03D0:                          D5 0C 80 F8 FF FF 7F F8          ........
03E0: FF FF 7F 63 74 65 78 00  80 00                    ...ctex...      
```

#### Opcodes

```
  0: 0x03D8 [0xD5] LOAD_EVENT_SCHEDULER_ALT8: Load scheduler "ct" with entities [EventEntity, EventEntity], work=ExtData[1]->WorkLocal[0]
  1: 0x03E9 [0x00] END_REQSTACK()
```

### Event 17

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
