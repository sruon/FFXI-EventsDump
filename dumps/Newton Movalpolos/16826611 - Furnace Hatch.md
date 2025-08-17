# 16826611 - Furnace Hatch

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Newton Movalpolos (ID: 12) |
| Block Size       | 104 bytes                  |
| Total Events     | 2                          |
| References Count | 4                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [22](#event-22)       | 0x0001       |     61 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001F      |          31 |
|       1 | 0x0000      |           0 |
|       2 | 0x00A0      |         160 |
|       3 | 0x005A      |          90 |

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

### Event 22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 61 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 20 01 45 00 80 F8  FF FF 7F F8 FF FF 7F 76   B .E..........v
0010: 62 6F 6E 01 80 45 02 80  F8 FF FF 7F F8 FF FF 7F  bon..E..........
0020: 31 32 62 6D 01 80 1C 03  80 45 00 80 F8 FF FF 7F  12bm.....E......
0030: F8 FF FF 7F 76 62 6F 66  01 80 20 00 21 00        ....vbof.. .!.  
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x0004 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "vbon" with entities [EventEntity, EventEntity], work=[31*, 0*]
  3: 0x0015 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "12bm" with entities [EventEntity, EventEntity], work=[160*, 0*]
  4: 0x0026 [0x1C] WAIT(90* ticks)
  5: 0x0029 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "vbof" with entities [EventEntity, EventEntity], work=[31*, 0*]
  6: 0x003A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  7: 0x003C [0x21] END_EVENT
  8: 0x003D [0x00] END_REQSTACK()
```
