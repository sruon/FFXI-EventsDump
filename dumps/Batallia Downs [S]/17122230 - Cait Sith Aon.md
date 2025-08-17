# 17122230 - Cait Sith Aon

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Batallia Downs [S] (ID: 84) |
| Block Size       | 180 bytes                   |
| Total Events     | 4                           |
| References Count | 6                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [21](#event-21)          | 0x0001       |      3 |              2 |
| [65535.1](#event-655351) | 0x0004       |     58 |              9 |
| [65535.2](#event-655352) | 0x003E       |     61 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0585      |        1413 |
|       1 | 0x0BB1      |        2993 |
|       2 | 0x06F1      |        1777 |
|       3 | 0x0020      |          32 |
|       4 | 0x0001      |           1 |
|       5 | 0x0078      |         120 |

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

### Event 21

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    33 01 00                                        3..            
```

#### Opcodes

```
  0: 0x0001 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0003 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 58 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             5B 00 80 F8  FF FF 7F F8 FF FF 7F 73      [..........s
0010: 61 6B 30 03 00 00 01 80  02 00 00 02 80 01 2E 00  ak0.............
0020: 08 00 00 03 80 39 00 00  1C 04 80 01 18 00 5B 00  .....9........[.
0030: 80 F8 FF FF 7F F8 FF FF  7F 73 61 6B 6B 00        .........sakk.  
```

#### Opcodes

```
  0: 0x0004 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sak0" with entities [EventEntity, EventEntity], work=1413*
  1: 0x0013 [0x03] ExtData[1]->WorkLocal[0] = 2993*
  2: 0x0018 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1777*) GOTO 0x002E
  3: 0x0020 [0x08] ExtData[1]->WorkLocal[0] -= 32*
  4: 0x0025 [0x39] SET_ENTITY_DIRECTION(direction=ExtData[1]->WorkLocal[0])
  5: 0x0028 [0x1C] WAIT(1* ticks)
  6: 0x002B [0x01] GOTO 0x0018
  7: 0x002E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sakk" with entities [EventEntity, EventEntity], work=1413*
  8: 0x003D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003E   |
| Data Size    | 61 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            1C 05                ..
0040: 80 5B 00 80 F8 FF FF 7F  F8 FF FF 7F 73 61 6B 30  .[..........sak0
0050: 03 00 00 02 80 02 00 00  01 80 01 6B 00 07 00 00  ...........k....
0060: 03 80 39 00 00 1C 04 80  01 55 00 5B 00 80 F8 FF  ..9......U.[....
0070: FF 7F F8 FF FF 7F 73 61  6B 6B 00                 ......sakk.     
```

#### Opcodes

```
  0: 0x003E [0x1C] WAIT(120* ticks)
  1: 0x0041 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sak0" with entities [EventEntity, EventEntity], work=1413*
  2: 0x0050 [0x03] ExtData[1]->WorkLocal[0] = 1777*
  3: 0x0055 [0x02] IF !(ExtData[1]->WorkLocal[0] == 2993*) GOTO 0x006B
  4: 0x005D [0x07] ExtData[1]->WorkLocal[0] += 32*
  5: 0x0062 [0x39] SET_ENTITY_DIRECTION(direction=ExtData[1]->WorkLocal[0])
  6: 0x0065 [0x1C] WAIT(1* ticks)
  7: 0x0068 [0x01] GOTO 0x0055
  8: 0x006B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sakk" with entities [EventEntity, EventEntity], work=1413*
  9: 0x007A [0x00] END_REQSTACK()
```
