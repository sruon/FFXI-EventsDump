# 16974375 - Escape Route

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Al Zahbi (ID: 48) |
| Block Size       | 156 bytes         |
| Total Events     | 2                 |
| References Count | 10                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [293](#event-293)     | 0x0001       |     89 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x008C      |         140 |
|       3 | 0x00C8      |         200 |
|       4 | 0x003C      |          60 |
|       5 | 0xFFFE9A94  |  4294875796 |
|       6 | 0x18C7C     |      101500 |
|       7 | 0xFFFFE890  |  4294961296 |
|       8 | 0x0400      |        1024 |
|       9 | 0x0002      |           2 |

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

### Event 293

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 89 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 62 00 80 F0 FF FF  7F F0 FF FF 7F 6D 61 69   Bb..........mai
0010: 6E 01 80 1C 02 80 45 03  80 F0 FF FF 7F F0 FF FF  n.....E.........
0020: 7F 66 64 6F 31 01 80 1C  04 80 47 00 05 80 06 80  .fdo1.....G.....
0030: 07 80 08 80 47 01 45 03  80 F0 FF FF 7F F0 FF FF  ....G.E.........
0040: 7F 66 64 69 31 01 80 62  09 80 F0 FF FF 7F F0 FF  .fdi1..b........
0050: FF 7F 6D 61 69 6E 01 80  21 00                    ..main..!.      
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
  2: 0x0013 [0x1C] WAIT(140* ticks)
  3: 0x0016 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x0027 [0x1C] WAIT(60* ticks)
  5: 0x002A [0x47] UPDATE_PLAYER_POS(-91.500*, 101.500*, -6.000*, yaw=90.0°*)
  6: 0x0034 [0x47] WAIT_PLAYER_POS_UPDATE
  7: 0x0036 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x0047 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[2*, 0*]
  9: 0x0058 [0x21] END_EVENT
 10: 0x0059 [0x00] END_REQSTACK()
```
