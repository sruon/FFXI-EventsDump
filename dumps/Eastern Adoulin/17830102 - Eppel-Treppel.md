# 17830102 - Eppel-Treppel

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Eastern Adoulin (ID: 257) |
| Block Size       | 276 bytes                 |
| Total Events     | 5                         |
| References Count | 12                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [523](#event-523)        | 0x0001       |     43 |              9 |
| [591](#event-591)        | 0x002C       |    121 |             21 |
| [90](#event-90)          | 0x00A5       |      1 |              1 |
| [65535.1](#event-655351) | 0x00A6       |     24 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x28F1      |       10481 |
|       2 | 0x28F2      |       10482 |
|       3 | 0x28F3      |       10483 |
|       4 | 0x0000      |           0 |
|       5 | 0x0001      |           1 |
|       6 | 0x00C8      |         200 |
|       7 | 0x0002      |           2 |
|       8 | 0xFFFEC0B4  |  4294885556 |
|       9 | 0x242F      |        9263 |
|      10 | 0xFFFEC049  |  4294885449 |
|      11 | 0x1031      |        4145 |

## String References

- **10481**: The Celennia Memorial Library contains relics of knowledge from ages past as well as the latest-watest illuminated publications. We can't grantaru access to unproven philistines, however. Sorry.
- **10482**: The Celennia Memorial Library contains relics of knowledge from ages past as well as the latest-watest illuminated publications. Would you care to enter this vastaru vault of knowledge?
- **10483**: Enter the library? [Yes./No.]

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

### Event 523

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 43 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 66 00 80 F8 FF  ...tlk0...#f....
0020: FF 7F F8 FF FF 7F 74 6C  6B 31 21 00              ......tlk1!.    
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=10481*)
    → "The Celennia Memorial Library contains relics of knowledge from ages past as well as the latest-watest illuminated publications. We can't grantaru access to unproven philistines, however. Sorry."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
  7: 0x002A [0x21] END_EVENT
  8: 0x002B [0x00] END_REQSTACK()
```

### Event 591

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x002C    |
| Data Size    | 121 bytes |
| Instructions | 20        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      1E F0 FF FF              ....
0030: 7F 6F 70 66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  .opf..........tl
0040: 6B 30 1D 02 80 23 24 03  80 04 80 04 80 25 02 00  k0...#$......%..
0050: 10 04 80 00 84 00 42 03  01 10 05 80 45 06 80 F0  ......B.....E...
0060: FF FF 7F F0 FF FF 7F 66  64 6F 31 04 80 55 06 80  .......fdo1..U..
0070: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 03 01 10 05  ........fdo1....
0080: 80 01 A3 00 02 00 10 05  80 00 A3 00 03 01 10 07  ................
0090: 80 01 A3 00 66 00 80 F8  FF FF 7F F8 FF FF 7F 74  ....f..........t
00A0: 6C 6B 31 21 00                                    lk1!.           
```

#### Opcodes

```
  0: 0x002C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0031 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0032 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0033 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  4: 0x0042 [0x1D] PRINT_EVENT_MESSAGE(message_id=10482*)
    → "The Celennia Memorial Library contains relics of knowledge from ages past as well as the latest-watest illuminated publications. Would you care to enter this vastaru vault of knowledge?"
  5: 0x0045 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0046 [0x24] CREATE_DIALOG(message_id=10483*, default_option=0*, option_flags=0*)
    → "Enter the library? [Yes./No.]"
  7: 0x004D [0x25] WAIT_DIALOG_SELECT()
  8: 0x004E [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0084
  9: 0x0056 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 10: 0x0057 [0x03] Work_Zone[1] = 1*
 11: 0x005C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 12: 0x006D [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 13: 0x007C [0x03] Work_Zone[1] = 1*
 14: 0x0081 [0x01] GOTO 0x00A3
 15: 0x0084 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00A3
 16: 0x008C [0x03] Work_Zone[1] = 2*
 17: 0x0091 [0x01] GOTO 0x00A3

SUBROUTINE_00A3:
 18: 0x00A3 [0x21] END_EVENT
 19: 0x00A4 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0094 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
```

### Event 90

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A5  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                00                                      .          
```

#### Opcodes

```
  0: 0x00A5 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A6   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                   32 00  80 1F 00 08 80 09 80 04        2.........
00B0: 80 1F 01 1F 00 0A 80 0B  80 04 80 1F 01 00        ..............  
```

#### Opcodes

```
  0: 0x00A6 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00A9 [0x1F] MOVE_ENTITY: EventEntity moves to X=-81.740*, Z=9.263*, Y=0.000*
  2: 0x00B1 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00B3 [0x1F] MOVE_ENTITY: EventEntity moves to X=-81.847*, Z=4.145*, Y=0.000*
  4: 0x00BB [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00BD [0x00] END_REQSTACK()
```
