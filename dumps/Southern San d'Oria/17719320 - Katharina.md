# 17719320 - Katharina

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 172 bytes                     |
| Total Events     | 3                             |
| References Count | 13                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     33 |              7 |
| [887](#event-887)        | 0x0022       |     57 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0046      |          70 |
|       1 | 0xFFFF670C  |  4294928140 |
|       2 | 0xFFFF51F6  |  4294922742 |
|       3 | 0x07D3      |        2003 |
|       4 | 0x0BAE      |        2990 |
|       5 | 0xFFFF5368  |  4294923112 |
|       6 | 0xFFFF67A0  |  4294928288 |
|       7 | 0x07CF      |        1999 |
|       8 | 0xFFFEC46D  |  4294886509 |
|       9 | 0xFFFFEC5F  |  4294962271 |
|      10 | 0x000A      |          10 |
|      11 | 0x203C      |        8252 |
|      12 | 0x203D      |        8253 |

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
| Data Size    | 33 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    32 00 80 37 01 80 02  80 03 80 04 80 1F 00 05   2..7...........
0010: 80 06 80 07 80 1F 01 1F  00 08 80 09 80 07 80 1F  ................
0020: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0001 [0x32] ExtData[1]->MainSpeed = 70* * 0.1
  1: 0x0004 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-39.156*, z=-44.554*, y=2.003*, direction=262.8°*
  2: 0x000D [0x1F] MOVE_ENTITY: EventEntity moves to X=-44.184*, Z=-39.008*, Y=1.999*
  3: 0x0015 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0017 [0x1F] MOVE_ENTITY: EventEntity moves to X=-80.787*, Z=-5.025*, Y=1.999*
  5: 0x001F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0021 [0x00] END_REQSTACK()
```

### Event 887

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0022   |
| Data Size    | 57 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       4A 18 60 0E 01 F0  FF FF 7F 66 0A 80 F8 FF    J.`......f....
0030: FF 7F F8 FF FF 7F 74 6C  6B 30 2B 18 60 0E 01 0B  ......tlk0+.`...
0040: 80 23 2B 18 60 0E 01 0C  80 23 66 0A 80 F8 FF FF  .#+.`....#f.....
0050: 7F F8 FF FF 7F 74 6C 6B  31 21 00                 .....tlk1!.     
```

#### Opcodes

```
  0: 0x0022 [0x4A] Katharina (ID: 17719320/0x010E6018) looks at LocalPlayer
  1: 0x002B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=10*
  2: 0x003A [0x2B] Katharina (ID: 17719320/0x010E6018) [8252*]:
    → "Come in! Come in! And welcome to the Lion Springs Tavern! Run by none other than the great hero of the Norvallen Resistance, Valderotaux himself."
  3: 0x0041 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0042 [0x2B] Katharina (ID: 17719320/0x010E6018) [8253*]:
    → "Make yourself at home! Can I interest you in some of our famous mulsum?"
  5: 0x0049 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x004A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=10*
  7: 0x0059 [0x21] END_EVENT
  8: 0x005A [0x00] END_REQSTACK()
```
