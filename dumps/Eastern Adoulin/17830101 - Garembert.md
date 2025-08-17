# 17830101 - Garembert

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Eastern Adoulin (ID: 257) |
| Block Size       | 148 bytes                 |
| Total Events     | 4                         |
| References Count | 10                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [522](#event-522)        | 0x0001       |     47 |             11 |
| [90](#event-90)          | 0x0030       |      1 |              1 |
| [65535.1](#event-655351) | 0x0031       |     24 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001D      |          29 |
|       1 | 0x28CE      |       10446 |
|       2 | 0x28CF      |       10447 |
|       3 | 0x0028      |          40 |
|       4 | 0xFFFEB2A1  |  4294881953 |
|       5 | 0x24AD      |        9389 |
|       6 | 0xFFFFFF6C  |  4294967148 |
|       7 | 0xFFFEC049  |  4294885449 |
|       8 | 0x1031      |        4145 |
|       9 | 0x0000      |           0 |

## String References

- **10446**: Oho, a sojourner come to experience the wonders of our fine city, are you? Eastern Adoulin surpasses even your wildest expectations for this mysterious continent, does it not?
- **10447**: I can say with certainty that our side of the city is vastly more dignified than the plebian slum... That is where the Pioneers' Coalition resides, however, so you'll have to brave the filth if you wish to register for the colonization effort.

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

### Event 522

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 47 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 68 6B 31 1D  01 80 23 66 00 80 F8 FF  ...thk1...#f....
0020: FF 7F F8 FF FF 7F 74 68  6B 32 1D 02 80 23 21 00  ......thk2...#!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=29*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=10446*)
    → "Oho, a sojourner come to experience the wonders of our fine city, are you? Eastern Adoulin surpasses even your wildest expectations for this mysterious continent, does it not?"
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=29*
  7: 0x002A [0x1D] PRINT_EVENT_MESSAGE(message_id=10447*)
    → "I can say with certainty that our side of the city is vastly more dignified than the plebian slum... That is where the Pioneers' Coalition resides, however, so you'll have to brave the filth if you wish to register for the colonization effort."
  8: 0x002D [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x002E [0x21] END_EVENT
 10: 0x002F [0x00] END_REQSTACK()
```

### Event 90

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0030  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0030 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0031   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    32 03 80 1F 00 04 80  05 80 06 80 1F 01 1F 00   2..............
0040: 07 80 08 80 09 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x0031 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0034 [0x1F] MOVE_ENTITY: EventEntity moves to X=-85.343*, Z=9.389*, Y=-0.148*
  2: 0x003C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003E [0x1F] MOVE_ENTITY: EventEntity moves to X=-81.847*, Z=4.145*, Y=0.000*
  4: 0x0046 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0048 [0x00] END_REQSTACK()
```
