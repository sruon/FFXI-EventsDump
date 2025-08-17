# 16826610 - Furnace Hatch

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Newton Movalpolos (ID: 12) |
| Block Size       | 140 bytes                  |
| Total Events     | 3                          |
| References Count | 7                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [20](#event-20)       | 0x0001       |     19 |              9 |
| [21](#event-21)       | 0x0014       |     61 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x03B3      |         947 |
|       1 | 0x1C52      |        7250 |
|       2 | 0x1C53      |        7251 |
|       3 | 0x001F      |          31 |
|       4 | 0x0000      |           0 |
|       5 | 0x00A0      |         160 |
|       6 | 0x005A      |          90 |

## String References

- **7250**: +++Zstay@back!++ ++++Zdanger!++++ +++Zvery@danger!+++ +Zno #!+
- **7251**: Whatever that's supposed to mean...

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

### Event 20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 19 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 03 02 10 00 80  48 01 80 23 48 02 80 23    ......H..#H..#
0010: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x03] Work_Zone[2] = 947*
  2: 0x0008 [0x48] [System] [7250*]:
    → "+++Zstay@back!++ ++++Zdanger!++++ +++Zvery@danger!+++ +Zno #!+"
  3: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000C [0x48] [System] [7251*]:
    → "Whatever that's supposed to mean..."
  5: 0x000F [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0010 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  7: 0x0012 [0x21] END_EVENT
  8: 0x0013 [0x00] END_REQSTACK()
```

### Event 21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 61 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             42 20 01 45  03 80 F8 FF FF 7F F8 FF      B .E........
0020: FF 7F 76 62 6F 6E 04 80  45 05 80 F8 FF FF 7F F8  ..vbon..E.......
0030: FF FF 7F 31 32 62 6D 04  80 1C 06 80 45 03 80 F8  ...12bm.....E...
0040: FF FF 7F F8 FF FF 7F 76  62 6F 66 04 80 20 00 21  .......vbof.. .!
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0014 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0015 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x0017 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "vbon" with entities [EventEntity, EventEntity], work=[31*, 0*]
  3: 0x0028 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "12bm" with entities [EventEntity, EventEntity], work=[160*, 0*]
  4: 0x0039 [0x1C] WAIT(90* ticks)
  5: 0x003C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "vbof" with entities [EventEntity, EventEntity], work=[31*, 0*]
  6: 0x004D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  7: 0x004F [0x21] END_EVENT
  8: 0x0050 [0x00] END_REQSTACK()
```
