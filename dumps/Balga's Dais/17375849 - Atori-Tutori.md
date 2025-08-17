# 17375849 - Atori-Tutori

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Balga's Dais (ID: 146) |
| Block Size       | 232 bytes              |
| Total Events     | 5                      |
| References Count | 12                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [32000](#event-32000)    | 0x0001       |      1 |              1 |
| [32001](#event-32001)    | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     14 |              4 |
| [65535.2](#event-655352) | 0x0011       |    128 |             23 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFFF1F6  |  4294963702 |
|       2 | 0x0813      |        2067 |
|       3 | 0xFFFFF9A8  |  4294965672 |
|       4 | 0x0028      |          40 |
|       5 | 0x001E      |          30 |
|       6 | 0x000F      |          15 |
|       7 | 0x05DC      |        1500 |
|       8 | 0xFFFFD8F0  |  4294957296 |
|       9 | 0x000A      |          10 |
|      10 | 0x0050      |          80 |
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

### Event 32000

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

### Event 32001

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
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          32 00 80 1F 00  01 80 02 80 03 80 1F 01     2............
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0003 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0006 [0x1F] MOVE_ENTITY: EventEntity moves to X=-3.594*, Z=2.067*, Y=-1.624*
  2: 0x000E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0011    |
| Data Size    | 128 bytes |
| Instructions | 23        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    33 01 03 00 00 00 7F  03 01 00 02 7F 03 02 00   3..............
0020: 01 7F 03 03 00 03 7F 03  04 00 01 7F 66 04 80 F8  ............f...
0030: FF FF 7F F8 FF FF 7F 6A  6D 70 30 1C 05 80 66 04  .......jmp0...f.
0040: 80 F8 FF FF 7F F8 FF FF  7F 6A 6D 70 33 1C 06 80  .........jmp3...
0050: 06 05 00 03 06 00 07 80  02 05 00 08 80 04 90 00  ................
0060: 03 02 00 04 00 07 02 00  05 00 37 00 00 01 00 02  ..........7.....
0070: 00 03 00 02 06 00 05 80  04 80 00 08 06 00 09 80  ................
0080: 08 00 00 0A 80 08 05 00  06 00 1C 0B 80 01 58 00  ..............X.
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x0011 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0013 [0x03] ExtData[1]->WorkLocal[0] = ExtData[1]->EventPos[0] * 1000.0
  2: 0x0018 [0x03] ExtData[1]->WorkLocal[1] = ExtData[1]->EventPos[2] * 1000.0
  3: 0x001D [0x03] ExtData[1]->WorkLocal[2] = ExtData[1]->EventPos[1] * 1000.0
  4: 0x0022 [0x03] ExtData[1]->WorkLocal[3] = enDirCli(ExtData[1]->EventDir[1]) * 4096.0 * 0.15915963
  5: 0x0027 [0x03] ExtData[1]->WorkLocal[4] = ExtData[1]->EventPos[1] * 1000.0
  6: 0x002C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "jmp0" with entities [EventEntity, EventEntity], work=40*
  7: 0x003B [0x1C] WAIT(30* ticks)
  8: 0x003E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "jmp3" with entities [EventEntity, EventEntity], work=40*
  9: 0x004D [0x1C] WAIT(15* ticks)
 10: 0x0050 [0x06] ExtData[1]->WorkLocal[5] = 0
 11: 0x0053 [0x03] ExtData[1]->WorkLocal[6] = 1500*
 12: 0x0058 [0x02] IF !(ExtData[1]->WorkLocal[5] < 4294957296*) GOTO 0x0090
 13: 0x0060 [0x03] ExtData[1]->WorkLocal[2] = ExtData[1]->WorkLocal[4]
 14: 0x0065 [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[5]
 15: 0x006A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[0], z=ExtData[1]->WorkLocal[1], y=ExtData[1]->WorkLocal[2], direction=ExtData[1]->WorkLocal[3]
 16: 0x0073 [0x02] IF !(ExtData[1]->WorkLocal[6] < 30*) GOTO 0x0080
 17: 0x007B [0x08] ExtData[1]->WorkLocal[6] -= 10*
 18: 0x0080 [0x08] ExtData[1]->WorkLocal[0] -= 80*
 19: 0x0085 [0x08] ExtData[1]->WorkLocal[5] -= ExtData[1]->WorkLocal[6]
 20: 0x008A [0x1C] WAIT(1* ticks)
 21: 0x008D [0x01] GOTO 0x0058
 22: 0x0090 [0x00] END_REQSTACK()
```
