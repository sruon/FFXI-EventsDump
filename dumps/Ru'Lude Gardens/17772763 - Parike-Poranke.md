# 17772763 - Parike-Poranke

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 480 bytes                 |
| Total Events     | 8                         |
| References Count | 20                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [10136](#event-10136)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     52 |              8 |
| [65535.2](#event-655352) | 0x0036       |     13 |              4 |
| [10137](#event-10137)    | 0x0043       |      1 |              1 |
| [10161](#event-10161)    | 0x0044       |      7 |              3 |
| [65535.3](#event-655353) | 0x004B       |    149 |             27 |
| [65535.4](#event-655354) | 0x00E0       |    126 |             23 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CED      |        7405 |
|       1 | 0x1CEC6     |      118470 |
|       2 | 0x0C1C      |        3100 |
|       3 | 0x0816      |        2070 |
|       4 | 0x1C5EB     |      116203 |
|       5 | 0x0C1D      |        3101 |
|       6 | 0x0000      |           0 |
|       7 | 0x0001      |           1 |
|       8 | 0x0004      |           4 |
|       9 | 0x000B      |          11 |
|      10 | 0x000C      |          12 |
|      11 | 0x0002      |           2 |
|      12 | 0x000D      |          13 |
|      13 | 0x0003      |           3 |
|      14 | 0x000E      |          14 |
|      15 | 0x012C      |         300 |
|      16 | 0x0005      |           5 |
|      17 | 0x0015      |          21 |
|      18 | 0x0019      |          25 |
|      19 | 0x001D      |          29 |

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

### Event 10136

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 52 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1F 00 00 80 01 80  02 80 1F 01 1E 75 30 0F    ...........u0.
0010: 01 4A F0 FF FF 7F DB 30  0F 01 4A 75 30 0F 01 DB  .J.....0..Ju0...
0020: 30 0F 01 4A 31 30 0F 01  DB 30 0F 01 4A DC 30 0F  0..J10...0..J.0.
0030: 01 DB 30 0F 01 00                                 ..0...          
```

#### Opcodes

```
  0: 0x0002 [0x1F] MOVE_ENTITY: EventEntity moves to X=7.405*, Z=118.470*, Y=3.100*
  1: 0x000A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x000C [0x1E] EventEntity looks at Nomad Moogle (ID: 17772661/0x010F3075) and starts talking
  3: 0x0011 [0x4A] LocalPlayer looks at Parike-Poranke (ID: 17772763/0x010F30DB)
  4: 0x001A [0x4A] Nomad Moogle (ID: 17772661/0x010F3075) looks at Parike-Poranke (ID: 17772763/0x010F30DB)
  5: 0x0023 [0x4A] Maat (ID: 17772593/0x010F3031) looks at Parike-Poranke (ID: 17772763/0x010F30DB)
  6: 0x002C [0x4A] Magian Moogle (ID: 17772764/0x010F30DC) looks at Parike-Poranke (ID: 17772763/0x010F30DB)
  7: 0x0035 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0036   |
| Data Size    | 13 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   1F 00  03 80 04 80 05 80 1F 01        ..........
0040: 22 01 00                                          "..             
```

#### Opcodes

```
  0: 0x0036 [0x1F] MOVE_ENTITY: EventEntity moves to X=2.070*, Z=116.203*, Y=3.101*
  1: 0x003E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0040 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  3: 0x0042 [0x00] END_REQSTACK()
```

### Event 10137

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0043  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          00                                          .            
```

#### Opcodes

```
  0: 0x0043 [0x00] END_REQSTACK()
```

### Event 10161

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0044  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             06 00 00 06  01 00 00                     .......     
```

#### Opcodes

```
  0: 0x0044 [0x06] ExtData[1]->WorkLocal[0] = 0
  1: 0x0047 [0x06] ExtData[1]->WorkLocal[1] = 0
  2: 0x004A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x004B    |
| Data Size    | 149 bytes |
| Instructions | 27        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   3C 21 10 06 80             <!...
0050: 07 80 02 00 00 06 80 00  D8 00 13 01 00 08 80 02  ................
0060: 01 00 06 80 80 76 00 6E  DB 30 0F 01 09 80 99 DB  .....v.n.0......
0070: 30 0F 01 01 D2 00 02 01  00 07 80 80 8D 00 6E DB  0.............n.
0080: 30 0F 01 0A 80 99 DB 30  0F 01 01 D2 00 02 01 00  0......0........
0090: 0B 80 80 A4 00 6E DB 30  0F 01 0C 80 99 DB 30 0F  .....n.0......0.
00A0: 01 01 D2 00 02 01 00 0D  80 80 BB 00 6E DB 30 0F  ............n.0.
00B0: 01 0E 80 99 DB 30 0F 01  01 D2 00 02 01 00 08 80  .....0..........
00C0: 80 D2 00 6E DB 30 0F 01  08 80 99 DB 30 0F 01 01  ...n.0......0...
00D0: D2 00 1C 0F 80 01 52 00  3D 21 10 06 80 07 80 00  ......R.=!......
```

#### Opcodes

```
  0: 0x004B [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=Work_Zone[33], bit_index_work_offset=0*, condition_work_offset=1*)
  1: 0x0052 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x00D8
  2: 0x005A [0x13] ExtData[1]->WorkLocal[1] = rand() % 4*
  3: 0x005F [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x0076
  4: 0x0067 [0x6E] Parike-Poranke (ID: 17772763/0x010F30DB) uses emote 11*
  5: 0x006E [0x99] Wait for Parike-Poranke (ID: 17772763/0x010F30DB) animation to complete
  6: 0x0073 [0x01] GOTO 0x00D2
  7: 0x0076 [0x02] IF !(ExtData[1]->WorkLocal[1] == 1*) GOTO 0x008D
  8: 0x007E [0x6E] Parike-Poranke (ID: 17772763/0x010F30DB) uses emote 12*
  9: 0x0085 [0x99] Wait for Parike-Poranke (ID: 17772763/0x010F30DB) animation to complete
 10: 0x008A [0x01] GOTO 0x00D2
 11: 0x008D [0x02] IF !(ExtData[1]->WorkLocal[1] == 2*) GOTO 0x00A4
 12: 0x0095 [0x6E] Parike-Poranke (ID: 17772763/0x010F30DB) uses emote 13*
 13: 0x009C [0x99] Wait for Parike-Poranke (ID: 17772763/0x010F30DB) animation to complete
 14: 0x00A1 [0x01] GOTO 0x00D2
 15: 0x00A4 [0x02] IF !(ExtData[1]->WorkLocal[1] == 3*) GOTO 0x00BB
 16: 0x00AC [0x6E] Parike-Poranke (ID: 17772763/0x010F30DB) uses emote 14*
 17: 0x00B3 [0x99] Wait for Parike-Poranke (ID: 17772763/0x010F30DB) animation to complete
 18: 0x00B8 [0x01] GOTO 0x00D2
 19: 0x00BB [0x02] IF !(ExtData[1]->WorkLocal[1] == 4*) GOTO 0x00D2
 20: 0x00C3 [0x6E] Parike-Poranke (ID: 17772763/0x010F30DB) uses emote 4*
 21: 0x00CA [0x99] Wait for Parike-Poranke (ID: 17772763/0x010F30DB) animation to complete
 22: 0x00CF [0x01] GOTO 0x00D2

SUBROUTINE_00D2:
 23: 0x00D2 [0x1C] WAIT(300* ticks)
 24: 0x00D5 [0x01] GOTO 0x0052
 25: 0x00D8 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=Work_Zone[33], bit_index_work_offset=0*, condition_work_offset=1*)
 26: 0x00DF [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00E0    |
| Data Size    | 126 bytes |
| Instructions | 23        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0: 3C 21 10 06 80 07 80 02  00 00 06 80 00 56 01 13  <!...........V..
00F0: 01 00 0D 80 02 01 00 06  80 80 0B 01 6E DB 30 0F  ............n.0.
0100: 01 10 80 99 DB 30 0F 01  01 50 01 02 01 00 07 80  .....0...P......
0110: 80 22 01 6E DB 30 0F 01  11 80 99 DB 30 0F 01 01  .".n.0......0...
0120: 50 01 02 01 00 0B 80 80  39 01 6E DB 30 0F 01 12  P.......9.n.0...
0130: 80 99 DB 30 0F 01 01 50  01 02 01 00 0D 80 80 50  ...0...P.......P
0140: 01 6E DB 30 0F 01 13 80  99 DB 30 0F 01 01 50 01  .n.0......0...P.
0150: 1C 0F 80 01 E7 00 3D 21  10 06 80 07 80 00        ......=!......  
```

#### Opcodes

```
  0: 0x00E0 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=Work_Zone[33], bit_index_work_offset=0*, condition_work_offset=1*)
  1: 0x00E7 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x0156
  2: 0x00EF [0x13] ExtData[1]->WorkLocal[1] = rand() % 3*
  3: 0x00F4 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x010B
  4: 0x00FC [0x6E] Parike-Poranke (ID: 17772763/0x010F30DB) uses emote 5*
  5: 0x0103 [0x99] Wait for Parike-Poranke (ID: 17772763/0x010F30DB) animation to complete
  6: 0x0108 [0x01] GOTO 0x0150
  7: 0x010B [0x02] IF !(ExtData[1]->WorkLocal[1] == 1*) GOTO 0x0122
  8: 0x0113 [0x6E] Parike-Poranke (ID: 17772763/0x010F30DB) uses emote 21*
  9: 0x011A [0x99] Wait for Parike-Poranke (ID: 17772763/0x010F30DB) animation to complete
 10: 0x011F [0x01] GOTO 0x0150
 11: 0x0122 [0x02] IF !(ExtData[1]->WorkLocal[1] == 2*) GOTO 0x0139
 12: 0x012A [0x6E] Parike-Poranke (ID: 17772763/0x010F30DB) uses emote 25*
 13: 0x0131 [0x99] Wait for Parike-Poranke (ID: 17772763/0x010F30DB) animation to complete
 14: 0x0136 [0x01] GOTO 0x0150
 15: 0x0139 [0x02] IF !(ExtData[1]->WorkLocal[1] == 3*) GOTO 0x0150
 16: 0x0141 [0x6E] Parike-Poranke (ID: 17772763/0x010F30DB) uses emote 29*
 17: 0x0148 [0x99] Wait for Parike-Poranke (ID: 17772763/0x010F30DB) animation to complete
 18: 0x014D [0x01] GOTO 0x0150

SUBROUTINE_0150:
 19: 0x0150 [0x1C] WAIT(300* ticks)
 20: 0x0153 [0x01] GOTO 0x00E7
 21: 0x0156 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=Work_Zone[33], bit_index_work_offset=0*, condition_work_offset=1*)
 22: 0x015D [0x00] END_REQSTACK()
```
