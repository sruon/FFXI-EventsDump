# 17805360 - Disjoined One

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Hall of the Gods (ID: 251) |
| Block Size       | 356 bytes                  |
| Total Events     | 4                          |
| References Count | 11                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [15](#event-15)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |    256 |             26 |
| [65535.2](#event-655352) | 0x0102       |     21 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x00E6      |         230 |
|       3 | 0x0002      |           2 |
|       4 | 0x0003      |           3 |
|       5 | 0x0004      |           4 |
|       6 | 0x0005      |           5 |
|       7 | 0x0006      |           6 |
|       8 | 0x0007      |           7 |
|       9 | 0x0008      |           8 |
|      10 | 0x0184      |         388 |

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

### Event 15

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
0000:       29 10 F0 FF FF 7F  16 02 02 10 00 80 80 28    )............(
0010: 00 B6 0B 00 80 03 10 01  80 02 80 02 80 02 80 02  ................
0020: 80 01 80 01 80 01 01 01  02 02 10 03 80 80 47 00  ..............G.
0030: B6 0B 03 80 03 10 01 80  02 80 02 80 02 80 02 80  ................
0040: 01 80 01 80 01 01 01 02  02 10 04 80 80 66 00 B6  .............f..
0050: 0B 04 80 03 10 01 80 02  80 02 80 02 80 02 80 01  ................
0060: 80 01 80 01 01 01 02 02  10 05 80 80 85 00 B6 0B  ................
0070: 05 80 03 10 01 80 02 80  02 80 02 80 02 80 01 80  ................
0080: 01 80 01 01 01 02 02 10  06 80 80 A4 00 B6 0B 06  ................
0090: 80 03 10 01 80 02 80 02  80 02 80 02 80 01 80 01  ................
00A0: 80 01 01 01 02 02 10 07  80 80 C3 00 B6 0B 07 80  ................
00B0: 03 10 01 80 02 80 02 80  02 80 02 80 01 80 01 80  ................
00C0: 01 01 01 02 02 10 08 80  80 E2 00 B6 0B 08 80 03  ................
00D0: 10 01 80 02 80 02 80 02  80 02 80 01 80 01 80 01  ................
00E0: 01 01 02 02 10 09 80 80  01 01 B6 0B 09 80 03 10  ................
00F0: 01 80 02 80 02 80 02 80  02 80 01 80 01 80 01 01  ................
0100: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0002 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=LocalPlayer, tag_num=0x16)
  1: 0x0009 [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x0028
  2: 0x0011 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=1*, hair=Work_Zone[3], head=0*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
  3: 0x0025 [0x01] GOTO 0x0101
  4: 0x0028 [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x0047
  5: 0x0030 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=2*, hair=Work_Zone[3], head=0*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
  6: 0x0044 [0x01] GOTO 0x0101
  7: 0x0047 [0x02] IF !(Work_Zone[2] == 3*) GOTO 0x0066
  8: 0x004F [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=Work_Zone[3], head=0*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
  9: 0x0063 [0x01] GOTO 0x0101
 10: 0x0066 [0x02] IF !(Work_Zone[2] == 4*) GOTO 0x0085
 11: 0x006E [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=4*, hair=Work_Zone[3], head=0*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
 12: 0x0082 [0x01] GOTO 0x0101
 13: 0x0085 [0x02] IF !(Work_Zone[2] == 5*) GOTO 0x00A4
 14: 0x008D [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=5*, hair=Work_Zone[3], head=0*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
 15: 0x00A1 [0x01] GOTO 0x0101
 16: 0x00A4 [0x02] IF !(Work_Zone[2] == 6*) GOTO 0x00C3
 17: 0x00AC [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=6*, hair=Work_Zone[3], head=0*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
 18: 0x00C0 [0x01] GOTO 0x0101
 19: 0x00C3 [0x02] IF !(Work_Zone[2] == 7*) GOTO 0x00E2
 20: 0x00CB [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=Work_Zone[3], head=0*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
 21: 0x00DF [0x01] GOTO 0x0101
 22: 0x00E2 [0x02] IF !(Work_Zone[2] == 8*) GOTO 0x0101
 23: 0x00EA [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=8*, hair=Work_Zone[3], head=0*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
 24: 0x00FE [0x01] GOTO 0x0101

SUBROUTINE_0101:
 25: 0x0101 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0102   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:       B6 0B 00 80 01 80  0A 80 02 80 02 80 02 80    ..............
0110: 02 80 01 80 01 80 00                              .......         
```

#### Opcodes

```
  0: 0x0102 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=1*, hair=0*, head=388*, body=230*, hands=230*, legs=230*, feet=230*, main=0*, sub=0*)
  1: 0x0116 [0x00] END_REQSTACK()
```
