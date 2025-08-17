# 17969929 - Disjoined One

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Reisenjima (ID: 291) |
| Block Size       | 1900 bytes           |
| Total Events     | 16                   |
| References Count | 34                   |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [2](#event-2)              | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |    256 |             26 |
| [65535.2](#event-655352)   | 0x0102       |    224 |             26 |
| [4](#event-4)              | 0x01E2       |      4 |              2 |
| [5](#event-5)              | 0x01E6       |      4 |              2 |
| [65535.3](#event-655353)   | 0x01EA       |     10 |              2 |
| [65535.4](#event-655354)   | 0x01F4       |     10 |              2 |
| [65535.5](#event-655355)   | 0x01FE       |     21 |              2 |
| [65535.6](#event-655356)   | 0x0213       |    249 |             25 |
| [65535.7](#event-655357)   | 0x030C       |    224 |             26 |
| [65535.8](#event-655358)   | 0x03EC       |    224 |             26 |
| [65535.9](#event-655359)   | 0x04CC       |      3 |              2 |
| [65535.10](#event-6553510) | 0x04CF       |      3 |              2 |
| [65535.11](#event-6553511) | 0x04D2       |    224 |             26 |
| [65535.12](#event-6553512) | 0x05B2       |    224 |             26 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x0002      |           2 |
|       3 | 0x0003      |           3 |
|       4 | 0x0004      |           4 |
|       5 | 0x0005      |           5 |
|       6 | 0x0006      |           6 |
|       7 | 0x0007      |           7 |
|       8 | 0x0008      |           8 |
|       9 | 0x008F      |         143 |
|      10 | 0x0099      |         153 |
|      11 | 0x00A3      |         163 |
|      12 | 0x00AD      |         173 |
|      13 | 0x00B7      |         183 |
|      14 | 0x00C1      |         193 |
|      15 | 0x00CB      |         203 |
|      16 | 0x0080      |         128 |
|      17 | 0x0184      |         388 |
|      18 | 0x00E6      |         230 |
|      19 | 0x014A      |         330 |
|      20 | 0x00B9      |         185 |
|      21 | 0x0091      |         145 |
|      22 | 0x009B      |         155 |
|      23 | 0x00A5      |         165 |
|      24 | 0x00AF      |         175 |
|      25 | 0x00C3      |         195 |
|      26 | 0x00CD      |         205 |
|      27 | 0x00D4      |         212 |
|      28 | 0x00DE      |         222 |
|      29 | 0x00E8      |         232 |
|      30 | 0x00F2      |         242 |
|      31 | 0x00FC      |         252 |
|      32 | 0x0106      |         262 |
|      33 | 0x0110      |         272 |

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

### Event 2

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

### Event 65535.1

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0002    |
| Data Size    | 256 bytes |
| Instructions | 26        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       29 10 F0 FF FF 7F  02 02 02 10 00 80 80 28    )............(
0010: 00 B6 0B 00 80 03 10 04  10 05 10 06 10 07 10 08  ................
0020: 10 01 80 01 80 01 01 01  02 02 10 02 80 80 47 00  ..............G.
0030: B6 0B 02 80 03 10 04 10  05 10 06 10 07 10 08 10  ................
0040: 01 80 01 80 01 01 01 02  02 10 03 80 80 66 00 B6  .............f..
0050: 0B 03 80 03 10 04 10 05  10 06 10 07 10 08 10 01  ................
0060: 80 01 80 01 01 01 02 02  10 04 80 80 85 00 B6 0B  ................
0070: 04 80 03 10 04 10 05 10  06 10 07 10 08 10 01 80  ................
0080: 01 80 01 01 01 02 02 10  05 80 80 A4 00 B6 0B 05  ................
0090: 80 03 10 04 10 05 10 06  10 07 10 08 10 01 80 01  ................
00A0: 80 01 01 01 02 02 10 06  80 80 C3 00 B6 0B 06 80  ................
00B0: 03 10 04 10 05 10 06 10  07 10 08 10 01 80 01 80  ................
00C0: 01 01 01 02 02 10 07 80  80 E2 00 B6 0B 07 80 03  ................
00D0: 10 04 10 05 10 06 10 07  10 08 10 01 80 01 80 01  ................
00E0: 01 01 02 02 10 08 80 80  01 01 B6 0B 08 80 03 10  ................
00F0: 04 10 05 10 06 10 07 10  08 10 01 80 01 80 01 01  ................
0100: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0002 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x02)
  1: 0x0009 [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x0028
  2: 0x0011 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=1*, hair=Work_Zone[3], head=Work_Zone[4], body=Work_Zone[5], hands=Work_Zone[6], legs=Work_Zone[7], feet=Work_Zone[8], main=0*, sub=0*)
  3: 0x0025 [0x01] GOTO 0x0101
  4: 0x0028 [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x0047
  5: 0x0030 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=2*, hair=Work_Zone[3], head=Work_Zone[4], body=Work_Zone[5], hands=Work_Zone[6], legs=Work_Zone[7], feet=Work_Zone[8], main=0*, sub=0*)
  6: 0x0044 [0x01] GOTO 0x0101
  7: 0x0047 [0x02] IF !(Work_Zone[2] == 3*) GOTO 0x0066
  8: 0x004F [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=Work_Zone[3], head=Work_Zone[4], body=Work_Zone[5], hands=Work_Zone[6], legs=Work_Zone[7], feet=Work_Zone[8], main=0*, sub=0*)
  9: 0x0063 [0x01] GOTO 0x0101
 10: 0x0066 [0x02] IF !(Work_Zone[2] == 4*) GOTO 0x0085
 11: 0x006E [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=4*, hair=Work_Zone[3], head=Work_Zone[4], body=Work_Zone[5], hands=Work_Zone[6], legs=Work_Zone[7], feet=Work_Zone[8], main=0*, sub=0*)
 12: 0x0082 [0x01] GOTO 0x0101
 13: 0x0085 [0x02] IF !(Work_Zone[2] == 5*) GOTO 0x00A4
 14: 0x008D [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=5*, hair=Work_Zone[3], head=Work_Zone[4], body=Work_Zone[5], hands=Work_Zone[6], legs=Work_Zone[7], feet=Work_Zone[8], main=0*, sub=0*)
 15: 0x00A1 [0x01] GOTO 0x0101
 16: 0x00A4 [0x02] IF !(Work_Zone[2] == 6*) GOTO 0x00C3
 17: 0x00AC [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=6*, hair=Work_Zone[3], head=Work_Zone[4], body=Work_Zone[5], hands=Work_Zone[6], legs=Work_Zone[7], feet=Work_Zone[8], main=0*, sub=0*)
 18: 0x00C0 [0x01] GOTO 0x0101
 19: 0x00C3 [0x02] IF !(Work_Zone[2] == 7*) GOTO 0x00E2
 20: 0x00CB [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=Work_Zone[3], head=Work_Zone[4], body=Work_Zone[5], hands=Work_Zone[6], legs=Work_Zone[7], feet=Work_Zone[8], main=0*, sub=0*)
 21: 0x00DF [0x01] GOTO 0x0101
 22: 0x00E2 [0x02] IF !(Work_Zone[2] == 8*) GOTO 0x0101
 23: 0x00EA [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=8*, hair=Work_Zone[3], head=Work_Zone[4], body=Work_Zone[5], hands=Work_Zone[6], legs=Work_Zone[7], feet=Work_Zone[8], main=0*, sub=0*)
 24: 0x00FE [0x01] GOTO 0x0101

SUBROUTINE_0101:
 25: 0x0101 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0102    |
| Data Size    | 224 bytes |
| Instructions | 26        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:       29 10 F0 FF FF 7F  02 02 02 10 00 80 80 24    )............$
0110: 01 5F 04 09 80 09 33 12  01 09 33 12 01 68 6E 64  ._....3...3..hnd
0120: 30 01 E1 01 02 02 10 02  80 80 3F 01 5F 04 0A 80  0.........?._...
0130: 09 33 12 01 09 33 12 01  68 6E 64 30 01 E1 01 02  .3...3..hnd0....
0140: 02 10 03 80 80 5A 01 5F  04 0B 80 09 33 12 01 09  .....Z._....3...
0150: 33 12 01 68 6E 64 30 01  E1 01 02 02 10 04 80 80  3..hnd0.........
0160: 75 01 5F 04 0C 80 09 33  12 01 09 33 12 01 68 6E  u._....3...3..hn
0170: 64 30 01 E1 01 02 02 10  05 80 80 90 01 5F 04 0D  d0..........._..
0180: 80 09 33 12 01 09 33 12  01 68 6E 64 30 01 E1 01  ..3...3..hnd0...
0190: 02 02 10 06 80 80 AB 01  5F 04 0D 80 09 33 12 01  ........_....3..
01A0: 09 33 12 01 68 6E 64 30  01 E1 01 02 02 10 07 80  .3..hnd0........
01B0: 80 C6 01 5F 04 0E 80 09  33 12 01 09 33 12 01 68  ..._....3...3..h
01C0: 6E 64 30 01 E1 01 02 02  10 08 80 80 E1 01 5F 04  nd0..........._.
01D0: 0F 80 09 33 12 01 09 33  12 01 68 6E 64 30 01 E1  ...3...3..hnd0..
01E0: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0102 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x02)
  1: 0x0109 [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x0124
  2: 0x0111 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=143*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="hnd0")
  3: 0x0121 [0x01] GOTO 0x01E1
  4: 0x0124 [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x013F
  5: 0x012C [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=153*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="hnd0")
  6: 0x013C [0x01] GOTO 0x01E1
  7: 0x013F [0x02] IF !(Work_Zone[2] == 3*) GOTO 0x015A
  8: 0x0147 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=163*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="hnd0")
  9: 0x0157 [0x01] GOTO 0x01E1
 10: 0x015A [0x02] IF !(Work_Zone[2] == 4*) GOTO 0x0175
 11: 0x0162 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=173*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="hnd0")
 12: 0x0172 [0x01] GOTO 0x01E1
 13: 0x0175 [0x02] IF !(Work_Zone[2] == 5*) GOTO 0x0190
 14: 0x017D [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=183*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="hnd0")
 15: 0x018D [0x01] GOTO 0x01E1
 16: 0x0190 [0x02] IF !(Work_Zone[2] == 6*) GOTO 0x01AB
 17: 0x0198 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=183*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="hnd0")
 18: 0x01A8 [0x01] GOTO 0x01E1
 19: 0x01AB [0x02] IF !(Work_Zone[2] == 7*) GOTO 0x01C6
 20: 0x01B3 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=193*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="hnd0")
 21: 0x01C3 [0x01] GOTO 0x01E1
 22: 0x01C6 [0x02] IF !(Work_Zone[2] == 8*) GOTO 0x01E1
 23: 0x01CE [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=203*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="hnd0")
 24: 0x01DE [0x01] GOTO 0x01E1

SUBROUTINE_01E1:
 25: 0x01E1 [0x00] END_REQSTACK()
```

### Event 4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01E2  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:       C0 00 80 00                                   ....          
```

#### Opcodes

```
  0: 0x01E2 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x01E5 [0x00] END_REQSTACK()
```

### Event 5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01E6  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:                   C0 00  80 00                          ....      
```

#### Opcodes

```
  0: 0x01E6 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x01E9 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01EA   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:                                6C F8 FF FF 7F 01            l.....
01F0: 80 00 80 00                                       ....            
```

#### Opcodes

```
  0: 0x01EA [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x01F3 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01F4   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:             6C F8 FF FF  7F 10 80 00 80 00            l.........  
```

#### Opcodes

```
  0: 0x01F4 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x01FD [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01FE   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:                                            B6 0B                ..
0200: 00 80 01 80 11 80 12 80  12 80 12 80 12 80 01 80  ................
0210: 01 80 00                                          ...             
```

#### Opcodes

```
  0: 0x01FE [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=1*, hair=0*, head=388*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
  1: 0x0212 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0213    |
| Data Size    | 249 bytes |
| Instructions | 25        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0210:          02 02 10 00 80  80 32 02 B6 0B 00 80 03     ......2......
0220: 10 01 80 13 80 14 80 12  80 12 80 01 80 01 80 01  ................
0230: 0B 03 02 02 10 02 80 80  51 02 B6 0B 02 80 03 10  ........Q.......
0240: 01 80 13 80 14 80 12 80  12 80 01 80 01 80 01 0B  ................
0250: 03 02 02 10 03 80 80 70  02 B6 0B 03 80 03 10 01  .......p........
0260: 80 13 80 14 80 12 80 12  80 01 80 01 80 01 0B 03  ................
0270: 02 02 10 04 80 80 8F 02  B6 0B 04 80 03 10 01 80  ................
0280: 13 80 14 80 12 80 12 80  01 80 01 80 01 0B 03 02  ................
0290: 02 10 05 80 80 AE 02 B6  0B 05 80 03 10 01 80 13  ................
02A0: 80 14 80 12 80 12 80 01  80 01 80 01 0B 03 02 02  ................
02B0: 10 06 80 80 CD 02 B6 0B  06 80 03 10 01 80 13 80  ................
02C0: 14 80 12 80 12 80 01 80  01 80 01 0B 03 02 02 10  ................
02D0: 07 80 80 EC 02 B6 0B 07  80 03 10 01 80 13 80 14  ................
02E0: 80 12 80 12 80 01 80 01  80 01 0B 03 02 02 10 08  ................
02F0: 80 80 0B 03 B6 0B 08 80  03 10 01 80 13 80 14 80  ................
0300: 12 80 12 80 01 80 01 80  01 0B 03 00              ............    
```

#### Opcodes

```
  0: 0x0213 [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x0232
  1: 0x021B [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=1*, hair=Work_Zone[3], head=0*, body=330*, hands=185*, legs=230*, feet=230*, main=0*, sub=0*)
  2: 0x022F [0x01] GOTO 0x030B
  3: 0x0232 [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x0251
  4: 0x023A [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=2*, hair=Work_Zone[3], head=0*, body=330*, hands=185*, legs=230*, feet=230*, main=0*, sub=0*)
  5: 0x024E [0x01] GOTO 0x030B
  6: 0x0251 [0x02] IF !(Work_Zone[2] == 3*) GOTO 0x0270
  7: 0x0259 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=Work_Zone[3], head=0*, body=330*, hands=185*, legs=230*, feet=230*, main=0*, sub=0*)
  8: 0x026D [0x01] GOTO 0x030B
  9: 0x0270 [0x02] IF !(Work_Zone[2] == 4*) GOTO 0x028F
 10: 0x0278 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=4*, hair=Work_Zone[3], head=0*, body=330*, hands=185*, legs=230*, feet=230*, main=0*, sub=0*)
 11: 0x028C [0x01] GOTO 0x030B
 12: 0x028F [0x02] IF !(Work_Zone[2] == 5*) GOTO 0x02AE
 13: 0x0297 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=5*, hair=Work_Zone[3], head=0*, body=330*, hands=185*, legs=230*, feet=230*, main=0*, sub=0*)
 14: 0x02AB [0x01] GOTO 0x030B
 15: 0x02AE [0x02] IF !(Work_Zone[2] == 6*) GOTO 0x02CD
 16: 0x02B6 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=6*, hair=Work_Zone[3], head=0*, body=330*, hands=185*, legs=230*, feet=230*, main=0*, sub=0*)
 17: 0x02CA [0x01] GOTO 0x030B
 18: 0x02CD [0x02] IF !(Work_Zone[2] == 7*) GOTO 0x02EC
 19: 0x02D5 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=Work_Zone[3], head=0*, body=330*, hands=185*, legs=230*, feet=230*, main=0*, sub=0*)
 20: 0x02E9 [0x01] GOTO 0x030B
 21: 0x02EC [0x02] IF !(Work_Zone[2] == 8*) GOTO 0x030B
 22: 0x02F4 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=8*, hair=Work_Zone[3], head=0*, body=330*, hands=185*, legs=230*, feet=230*, main=0*, sub=0*)
 23: 0x0308 [0x01] GOTO 0x030B

SUBROUTINE_030B:
 24: 0x030B [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x030C    |
| Data Size    | 224 bytes |
| Instructions | 26        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0300:                                      29 10 F0 FF              )...
0310: FF 7F 02 02 02 10 00 80  80 2E 03 5F 04 15 80 09  ..........._....
0320: 33 12 01 09 33 12 01 62  75 6E 31 01 EB 03 02 02  3...3..bun1.....
0330: 10 02 80 80 49 03 5F 04  16 80 09 33 12 01 09 33  ....I._....3...3
0340: 12 01 62 75 6E 31 01 EB  03 02 02 10 03 80 80 64  ..bun1.........d
0350: 03 5F 04 17 80 09 33 12  01 09 33 12 01 62 75 6E  ._....3...3..bun
0360: 31 01 EB 03 02 02 10 04  80 80 7F 03 5F 04 18 80  1..........._...
0370: 09 33 12 01 09 33 12 01  62 75 6E 31 01 EB 03 02  .3...3..bun1....
0380: 02 10 05 80 80 9A 03 5F  04 14 80 09 33 12 01 09  ......._....3...
0390: 33 12 01 62 75 6E 31 01  EB 03 02 02 10 06 80 80  3..bun1.........
03A0: B5 03 5F 04 14 80 09 33  12 01 09 33 12 01 62 75  .._....3...3..bu
03B0: 6E 31 01 EB 03 02 02 10  07 80 80 D0 03 5F 04 19  n1..........._..
03C0: 80 09 33 12 01 09 33 12  01 62 75 6E 31 01 EB 03  ..3...3..bun1...
03D0: 02 02 10 08 80 80 EB 03  5F 04 1A 80 09 33 12 01  ........_....3..
03E0: 09 33 12 01 62 75 6E 31  01 EB 03 00              .3..bun1....    
```

#### Opcodes

```
  0: 0x030C [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x02)
  1: 0x0313 [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x032E
  2: 0x031B [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=145*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="bun1")
  3: 0x032B [0x01] GOTO 0x03EB
  4: 0x032E [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x0349
  5: 0x0336 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=155*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="bun1")
  6: 0x0346 [0x01] GOTO 0x03EB
  7: 0x0349 [0x02] IF !(Work_Zone[2] == 3*) GOTO 0x0364
  8: 0x0351 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=165*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="bun1")
  9: 0x0361 [0x01] GOTO 0x03EB
 10: 0x0364 [0x02] IF !(Work_Zone[2] == 4*) GOTO 0x037F
 11: 0x036C [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=175*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="bun1")
 12: 0x037C [0x01] GOTO 0x03EB
 13: 0x037F [0x02] IF !(Work_Zone[2] == 5*) GOTO 0x039A
 14: 0x0387 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=185*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="bun1")
 15: 0x0397 [0x01] GOTO 0x03EB
 16: 0x039A [0x02] IF !(Work_Zone[2] == 6*) GOTO 0x03B5
 17: 0x03A2 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=185*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="bun1")
 18: 0x03B2 [0x01] GOTO 0x03EB
 19: 0x03B5 [0x02] IF !(Work_Zone[2] == 7*) GOTO 0x03D0
 20: 0x03BD [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=195*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="bun1")
 21: 0x03CD [0x01] GOTO 0x03EB
 22: 0x03D0 [0x02] IF !(Work_Zone[2] == 8*) GOTO 0x03EB
 23: 0x03D8 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=205*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="bun1")
 24: 0x03E8 [0x01] GOTO 0x03EB

SUBROUTINE_03EB:
 25: 0x03EB [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x03EC    |
| Data Size    | 224 bytes |
| Instructions | 26        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03E0:                                      29 10 F0 FF              )...
03F0: FF 7F 02 02 02 10 00 80  80 0E 04 5F 04 15 80 09  ..........._....
0400: 33 12 01 09 33 12 01 74  72 69 30 01 CB 04 02 02  3...3..tri0.....
0410: 10 02 80 80 29 04 5F 04  16 80 09 33 12 01 09 33  ....)._....3...3
0420: 12 01 74 72 69 30 01 CB  04 02 02 10 03 80 80 44  ..tri0.........D
0430: 04 5F 04 17 80 09 33 12  01 09 33 12 01 74 72 69  ._....3...3..tri
0440: 30 01 CB 04 02 02 10 04  80 80 5F 04 5F 04 18 80  0........._._...
0450: 09 33 12 01 09 33 12 01  74 72 69 30 01 CB 04 02  .3...3..tri0....
0460: 02 10 05 80 80 7A 04 5F  04 14 80 09 33 12 01 09  .....z._....3...
0470: 33 12 01 74 72 69 30 01  CB 04 02 02 10 06 80 80  3..tri0.........
0480: 95 04 5F 04 14 80 09 33  12 01 09 33 12 01 74 72  .._....3...3..tr
0490: 69 30 01 CB 04 02 02 10  07 80 80 B0 04 5F 04 19  i0..........._..
04A0: 80 09 33 12 01 09 33 12  01 74 72 69 30 01 CB 04  ..3...3..tri0...
04B0: 02 02 10 08 80 80 CB 04  5F 04 1A 80 09 33 12 01  ........_....3..
04C0: 09 33 12 01 74 72 69 30  01 CB 04 00              .3..tri0....    
```

#### Opcodes

```
  0: 0x03EC [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x02)
  1: 0x03F3 [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x040E
  2: 0x03FB [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=145*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="tri0")
  3: 0x040B [0x01] GOTO 0x04CB
  4: 0x040E [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x0429
  5: 0x0416 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=155*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="tri0")
  6: 0x0426 [0x01] GOTO 0x04CB
  7: 0x0429 [0x02] IF !(Work_Zone[2] == 3*) GOTO 0x0444
  8: 0x0431 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=165*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="tri0")
  9: 0x0441 [0x01] GOTO 0x04CB
 10: 0x0444 [0x02] IF !(Work_Zone[2] == 4*) GOTO 0x045F
 11: 0x044C [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=175*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="tri0")
 12: 0x045C [0x01] GOTO 0x04CB
 13: 0x045F [0x02] IF !(Work_Zone[2] == 5*) GOTO 0x047A
 14: 0x0467 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=185*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="tri0")
 15: 0x0477 [0x01] GOTO 0x04CB
 16: 0x047A [0x02] IF !(Work_Zone[2] == 6*) GOTO 0x0495
 17: 0x0482 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=185*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="tri0")
 18: 0x0492 [0x01] GOTO 0x04CB
 19: 0x0495 [0x02] IF !(Work_Zone[2] == 7*) GOTO 0x04B0
 20: 0x049D [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=195*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="tri0")
 21: 0x04AD [0x01] GOTO 0x04CB
 22: 0x04B0 [0x02] IF !(Work_Zone[2] == 8*) GOTO 0x04CB
 23: 0x04B8 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=205*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="tri0")
 24: 0x04C8 [0x01] GOTO 0x04CB

SUBROUTINE_04CB:
 25: 0x04CB [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x04CC  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
04C0:                                      AB 08 00                 ... 
```

#### Opcodes

```
  0: 0x04CC [0xAB] EventEntity->Render.Flags2 |= 0x02 // Set bit 1
  1: 0x04CE [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x04CF  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
04C0:                                               AB                 .
04D0: 07 00                                             ..              
```

#### Opcodes

```
  0: 0x04CF [0xAB] EventEntity->Render.Flags2 |= 0x01 // Set bit 0
  1: 0x04D1 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x04D2    |
| Data Size    | 224 bytes |
| Instructions | 26        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
04D0:       29 10 F0 FF FF 7F  02 02 02 10 00 80 80 F4    ).............
04E0: 04 5F 04 1B 80 09 33 12  01 09 33 12 01 66 72 61  ._....3...3..fra
04F0: 30 01 B1 05 02 02 10 02  80 80 0F 05 5F 04 1C 80  0..........._...
0500: 09 33 12 01 09 33 12 01  66 72 61 30 01 B1 05 02  .3...3..fra0....
0510: 02 10 03 80 80 2A 05 5F  04 1D 80 09 33 12 01 09  .....*._....3...
0520: 33 12 01 66 72 61 30 01  B1 05 02 02 10 04 80 80  3..fra0.........
0530: 45 05 5F 04 1E 80 09 33  12 01 09 33 12 01 66 72  E._....3...3..fr
0540: 61 30 01 B1 05 02 02 10  05 80 80 60 05 5F 04 1F  a0.........`._..
0550: 80 09 33 12 01 09 33 12  01 66 72 61 30 01 B1 05  ..3...3..fra0...
0560: 02 02 10 06 80 80 7B 05  5F 04 1F 80 09 33 12 01  ......{._....3..
0570: 09 33 12 01 66 72 61 30  01 B1 05 02 02 10 07 80  .3..fra0........
0580: 80 96 05 5F 04 20 80 09  33 12 01 09 33 12 01 66  ..._. ..3...3..f
0590: 72 61 30 01 B1 05 02 02  10 08 80 80 B1 05 5F 04  ra0..........._.
05A0: 21 80 09 33 12 01 09 33  12 01 66 72 61 30 01 B1  !..3...3..fra0..
05B0: 05 00                                             ..              
```

#### Opcodes

```
  0: 0x04D2 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x02)
  1: 0x04D9 [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x04F4
  2: 0x04E1 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=212*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="fra0")
  3: 0x04F1 [0x01] GOTO 0x05B1
  4: 0x04F4 [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x050F
  5: 0x04FC [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=222*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="fra0")
  6: 0x050C [0x01] GOTO 0x05B1
  7: 0x050F [0x02] IF !(Work_Zone[2] == 3*) GOTO 0x052A
  8: 0x0517 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=232*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="fra0")
  9: 0x0527 [0x01] GOTO 0x05B1
 10: 0x052A [0x02] IF !(Work_Zone[2] == 4*) GOTO 0x0545
 11: 0x0532 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=242*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="fra0")
 12: 0x0542 [0x01] GOTO 0x05B1
 13: 0x0545 [0x02] IF !(Work_Zone[2] == 5*) GOTO 0x0560
 14: 0x054D [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=252*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="fra0")
 15: 0x055D [0x01] GOTO 0x05B1
 16: 0x0560 [0x02] IF !(Work_Zone[2] == 6*) GOTO 0x057B
 17: 0x0568 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=252*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="fra0")
 18: 0x0578 [0x01] GOTO 0x05B1
 19: 0x057B [0x02] IF !(Work_Zone[2] == 7*) GOTO 0x0596
 20: 0x0583 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=262*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="fra0")
 21: 0x0593 [0x01] GOTO 0x05B1
 22: 0x0596 [0x02] IF !(Work_Zone[2] == 8*) GOTO 0x05B1
 23: 0x059E [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=272*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="fra0")
 24: 0x05AE [0x01] GOTO 0x05B1

SUBROUTINE_05B1:
 25: 0x05B1 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x05B2    |
| Data Size    | 224 bytes |
| Instructions | 26        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
05B0:       29 10 F0 FF FF 7F  02 02 02 10 00 80 80 D4    ).............
05C0: 05 5F 04 1B 80 09 33 12  01 09 33 12 01 66 72 61  ._....3...3..fra
05D0: 31 01 91 06 02 02 10 02  80 80 EF 05 5F 04 1C 80  1..........._...
05E0: 09 33 12 01 09 33 12 01  66 72 61 31 01 91 06 02  .3...3..fra1....
05F0: 02 10 03 80 80 0A 06 5F  04 1D 80 09 33 12 01 09  ......._....3...
0600: 33 12 01 66 72 61 31 01  91 06 02 02 10 04 80 80  3..fra1.........
0610: 25 06 5F 04 1E 80 09 33  12 01 09 33 12 01 66 72  %._....3...3..fr
0620: 61 31 01 91 06 02 02 10  05 80 80 40 06 5F 04 1F  a1.........@._..
0630: 80 09 33 12 01 09 33 12  01 66 72 61 31 01 91 06  ..3...3..fra1...
0640: 02 02 10 06 80 80 5B 06  5F 04 1F 80 09 33 12 01  ......[._....3..
0650: 09 33 12 01 66 72 61 31  01 91 06 02 02 10 07 80  .3..fra1........
0660: 80 76 06 5F 04 20 80 09  33 12 01 09 33 12 01 66  .v._. ..3...3..f
0670: 72 61 31 01 91 06 02 02  10 08 80 80 91 06 5F 04  ra1..........._.
0680: 21 80 09 33 12 01 09 33  12 01 66 72 61 31 01 91  !..3...3..fra1..
0690: 06 00                                             ..              
```

#### Opcodes

```
  0: 0x05B2 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x02)
  1: 0x05B9 [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x05D4
  2: 0x05C1 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=212*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="fra1")
  3: 0x05D1 [0x01] GOTO 0x0691
  4: 0x05D4 [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x05EF
  5: 0x05DC [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=222*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="fra1")
  6: 0x05EC [0x01] GOTO 0x0691
  7: 0x05EF [0x02] IF !(Work_Zone[2] == 3*) GOTO 0x060A
  8: 0x05F7 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=232*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="fra1")
  9: 0x0607 [0x01] GOTO 0x0691
 10: 0x060A [0x02] IF !(Work_Zone[2] == 4*) GOTO 0x0625
 11: 0x0612 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=242*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="fra1")
 12: 0x0622 [0x01] GOTO 0x0691
 13: 0x0625 [0x02] IF !(Work_Zone[2] == 5*) GOTO 0x0640
 14: 0x062D [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=252*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="fra1")
 15: 0x063D [0x01] GOTO 0x0691
 16: 0x0640 [0x02] IF !(Work_Zone[2] == 6*) GOTO 0x065B
 17: 0x0648 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=252*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="fra1")
 18: 0x0658 [0x01] GOTO 0x0691
 19: 0x065B [0x02] IF !(Work_Zone[2] == 7*) GOTO 0x0676
 20: 0x0663 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=262*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="fra1")
 21: 0x0673 [0x01] GOTO 0x0691
 22: 0x0676 [0x02] IF !(Work_Zone[2] == 8*) GOTO 0x0691
 23: 0x067E [0x5F] MULTI_HANDLER_COMPLEX(mode=0x04 - Load ext scheduler (OpCode 0x5B mode 1), ref=272*, entity1=Disjoined One (ID: 17969929/0x01123309), entity2=Disjoined One (ID: 17969929/0x01123309), string="fra1")
 24: 0x068E [0x01] GOTO 0x0691

SUBROUTINE_0691:
 25: 0x0691 [0x00] END_REQSTACK()
```
