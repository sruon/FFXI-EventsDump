# 17846818 - Mnemonic Pool

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Ceizak Battlegrounds (ID: 261) |
| Block Size       | 384 bytes                      |
| Total Events     | 5                              |
| References Count | 12                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [31](#event-31)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |    148 |             20 |
| [65535.2](#event-655352) | 0x0096       |    101 |             11 |
| [65535.3](#event-655353) | 0x00FB       |     46 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0015      |          21 |
|       1 | 0x0014      |          20 |
|       2 | 0x000A      |          10 |
|       3 | 0x0019      |          25 |
|       4 | 0x003C      |          60 |
|       5 | 0x005A      |          90 |
|       6 | 0x00EF      |         239 |
|       7 | 0x0000      |           0 |
|       8 | 0x0028      |          40 |
|       9 | 0x001E      |          30 |
|      10 | 0x012C      |         300 |
|      11 | 0x0001      |           1 |

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

### Event 31

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
| Data Size    | 148 bytes |
| Instructions | 20        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       73 00 80 22 52 10  01 25 52 10 01 1C 01 80    s.."R..%R.....
0010: 73 00 80 22 52 10 01 26  52 10 01 1C 02 80 73 00  s.."R..&R.....s.
0020: 80 22 52 10 01 27 52 10  01 1C 03 80 73 00 80 22  ."R..'R.....s.."
0030: 52 10 01 28 52 10 01 1C  04 80 73 00 80 22 52 10  R..(R.....s.."R.
0040: 01 29 52 10 01 1C 05 80  2C 25 52 10 01 25 52 10  .)R.....,%R..%R.
0050: 01 64 65 61 64 1C 01 80  2C 26 52 10 01 26 52 10  .dead...,&R..&R.
0060: 01 64 65 61 64 1C 02 80  2C 27 52 10 01 27 52 10  .dead...,'R..'R.
0070: 01 64 65 61 64 1C 03 80  2C 28 52 10 01 28 52 10  .dead...,(R..(R.
0080: 01 64 65 61 64 1C 04 80  2C 29 52 10 01 29 52 10  .dead...,)R..)R.
0090: 01 64 65 61 64 00                                 .dead.          
```

#### Opcodes

```
  0: 0x0002 [0x73] Mnemonic Pool (ID: 17846818/0x01105222) casts magic 21* on Unnamed NPC (ID: 17846821/0x01105225)
  1: 0x000D [0x1C] WAIT(20* ticks)
  2: 0x0010 [0x73] Mnemonic Pool (ID: 17846818/0x01105222) casts magic 21* on Unnamed NPC (ID: 17846822/0x01105226)
  3: 0x001B [0x1C] WAIT(10* ticks)
  4: 0x001E [0x73] Mnemonic Pool (ID: 17846818/0x01105222) casts magic 21* on Unnamed NPC (ID: 17846823/0x01105227)
  5: 0x0029 [0x1C] WAIT(25* ticks)
  6: 0x002C [0x73] Mnemonic Pool (ID: 17846818/0x01105222) casts magic 21* on Unnamed NPC (ID: 17846824/0x01105228)
  7: 0x0037 [0x1C] WAIT(60* ticks)
  8: 0x003A [0x73] Mnemonic Pool (ID: 17846818/0x01105222) casts magic 21* on Unnamed NPC (ID: 17846825/0x01105229)
  9: 0x0045 [0x1C] WAIT(90* ticks)
 10: 0x0048 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "dead" with entities [Unnamed NPC (ID: 17846821/0x01105225), Unnamed NPC (ID: 17846821/0x01105225)]
 11: 0x0055 [0x1C] WAIT(20* ticks)
 12: 0x0058 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "dead" with entities [Unnamed NPC (ID: 17846822/0x01105226), Unnamed NPC (ID: 17846822/0x01105226)]
 13: 0x0065 [0x1C] WAIT(10* ticks)
 14: 0x0068 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "dead" with entities [Unnamed NPC (ID: 17846823/0x01105227), Unnamed NPC (ID: 17846823/0x01105227)]
 15: 0x0075 [0x1C] WAIT(25* ticks)
 16: 0x0078 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "dead" with entities [Unnamed NPC (ID: 17846824/0x01105228), Unnamed NPC (ID: 17846824/0x01105228)]
 17: 0x0085 [0x1C] WAIT(60* ticks)
 18: 0x0088 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "dead" with entities [Unnamed NPC (ID: 17846825/0x01105229), Unnamed NPC (ID: 17846825/0x01105229)]
 19: 0x0095 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0096    |
| Data Size    | 101 bytes |
| Instructions | 11        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                   BB 06  80 25 52 10 01 25 52 10        ...%R..%R.
00A0: 01 73 74 70 31 07 80 1C  08 80 BB 06 80 26 52 10  .stp1........&R.
00B0: 01 26 52 10 01 73 74 70  31 07 80 1C 01 80 BB 06  .&R..stp1.......
00C0: 80 27 52 10 01 27 52 10  01 73 74 70 31 07 80 1C  .'R..'R..stp1...
00D0: 09 80 BB 06 80 28 52 10  01 28 52 10 01 73 74 70  .....(R..(R..stp
00E0: 31 07 80 1C 04 80 BB 06  80 29 52 10 01 29 52 10  1........)R..)R.
00F0: 01 73 74 70 31 07 80 1C  0A 80 00                 .stp1......     
```

#### Opcodes

```
  0: 0x0096 [0xBB] LOAD_EVENT_SCHEDULER_ALT: Load scheduler "stp1" with entities [Unnamed NPC (ID: 17846821/0x01105225), Unnamed NPC (ID: 17846821/0x01105225)], work=[239*, 0*]
  1: 0x00A7 [0x1C] WAIT(40* ticks)
  2: 0x00AA [0xBB] LOAD_EVENT_SCHEDULER_ALT: Load scheduler "stp1" with entities [Unnamed NPC (ID: 17846822/0x01105226), Unnamed NPC (ID: 17846822/0x01105226)], work=[239*, 0*]
  3: 0x00BB [0x1C] WAIT(20* ticks)
  4: 0x00BE [0xBB] LOAD_EVENT_SCHEDULER_ALT: Load scheduler "stp1" with entities [Unnamed NPC (ID: 17846823/0x01105227), Unnamed NPC (ID: 17846823/0x01105227)], work=[239*, 0*]
  5: 0x00CF [0x1C] WAIT(30* ticks)
  6: 0x00D2 [0xBB] LOAD_EVENT_SCHEDULER_ALT: Load scheduler "stp1" with entities [Unnamed NPC (ID: 17846824/0x01105228), Unnamed NPC (ID: 17846824/0x01105228)], work=[239*, 0*]
  7: 0x00E3 [0x1C] WAIT(60* ticks)
  8: 0x00E6 [0xBB] LOAD_EVENT_SCHEDULER_ALT: Load scheduler "stp1" with entities [Unnamed NPC (ID: 17846825/0x01105229), Unnamed NPC (ID: 17846825/0x01105229)], work=[239*, 0*]
  9: 0x00F7 [0x1C] WAIT(300* ticks)
 10: 0x00FA [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FB   |
| Data Size    | 46 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                   6C 25 52 10 01             l%R..
0100: 07 80 0B 80 6C 26 52 10  01 07 80 0B 80 6C 27 52  ....l&R......l'R
0110: 10 01 07 80 0B 80 6C 28  52 10 01 07 80 0B 80 6C  ......l(R......l
0120: 29 52 10 01 07 80 0B 80  00                       )R.......       
```

#### Opcodes

```
  0: 0x00FB [0x6C] FADE_ENTITY_COLOR(entity_id=Unnamed NPC (ID: 17846821/0x01105225), end_alpha=0*, fade_time=1*)
  1: 0x0104 [0x6C] FADE_ENTITY_COLOR(entity_id=Unnamed NPC (ID: 17846822/0x01105226), end_alpha=0*, fade_time=1*)
  2: 0x010D [0x6C] FADE_ENTITY_COLOR(entity_id=Unnamed NPC (ID: 17846823/0x01105227), end_alpha=0*, fade_time=1*)
  3: 0x0116 [0x6C] FADE_ENTITY_COLOR(entity_id=Unnamed NPC (ID: 17846824/0x01105228), end_alpha=0*, fade_time=1*)
  4: 0x011F [0x6C] FADE_ENTITY_COLOR(entity_id=Unnamed NPC (ID: 17846825/0x01105229), end_alpha=0*, fade_time=1*)
  5: 0x0128 [0x00] END_REQSTACK()
```
