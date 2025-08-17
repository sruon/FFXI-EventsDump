# 17134075 - Red Canyon

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Bastok Markets [S] (ID: 87) |
| Block Size       | 296 bytes                   |
| Total Events     | 4                           |
| References Count | 16                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [358](#event-358)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     14 |              4 |
| [200](#event-200)        | 0x0010       |    184 |             38 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFC3180  |  4294717824 |
|       2 | 0xFFFF3D6C  |  4294917484 |
|       3 | 0xFFFFD121  |  4294955297 |
|       4 | 0x2A52      |       10834 |
|       5 | 0x2A53      |       10835 |
|       6 | 0x2A54      |       10836 |
|       7 | 0x0001      |           1 |
|       8 | 0x0000      |           0 |
|       9 | 0x00C8      |         200 |
|      10 | 0x003C      |          60 |
|      11 | 0x0013      |          19 |
|      12 | 0x04D3      |        1235 |
|      13 | 0x00D9      |         217 |
|      14 | 0x005A      |          90 |
|      15 | 0x00B4      |         180 |

## String References

- **10834**: Port Bastok is strictly off-limits to all but authorized personnel.
- **10835**: However, if you wish to travel to North Gustaberg, you may use the Republic's supply causeway.
- **10836**: Cross the bridge? [Yes./No.]

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

### Event 358

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
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=-249.472*, Z=-49.812*, Y=-11.999*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x00] END_REQSTACK()
```

### Event 200

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0010    |
| Data Size    | 184 bytes |
| Instructions | 38        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 20 01 1E F0 FF FF 7F 6F  70 1D 04 80 23 1D 05 80   ......op...#...
0020: 23 24 06 80 07 80 08 80  25 02 00 10 08 80 00 B4  #$......%.......
0030: 00 43 00 43 01 46 01 42  45 09 80 F0 FF FF 7F F0  .C.C.F.BE.......
0040: FF FF 7F 66 64 6F 31 08  80 1C 0A 80 38 0B 80 4B  ...fdo1.....8..K
0050: F8 FF FF 7F 0C 80 45 0D  80 F0 FF FF 7F F0 FF FF  ......E.........
0060: 7F 7A 38 37 61 08 80 29  01 F0 FF FF 7F 05 45 09  .z87a..)......E.
0070: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 31 08 80 1C  .........fdi1...
0080: 0A 80 27 01 FA 71 05 01  03 1C 0E 80 27 01 F0 FF  ..'..q......'...
0090: FF 7F 06 1C 0F 80 45 09  80 F0 FF FF 7F F0 FF FF  ......E.........
00A0: 7F 66 64 6F 31 08 80 1C  0A 80 03 01 10 07 80 46  .fdo1..........F
00B0: 00 01 C4 00 02 00 10 07  80 00 C4 00 03 01 10 08  ................
00C0: 80 01 C4 00 20 00 21 00                           .... .!.        
```

#### Opcodes

```
  0: 0x0010 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0012 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0017 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0018 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0019 [0x1D] PRINT_EVENT_MESSAGE(message_id=10834*)
    → "Port Bastok is strictly off-limits to all but authorized personnel."
  5: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001D [0x1D] PRINT_EVENT_MESSAGE(message_id=10835*)
    → "However, if you wish to travel to North Gustaberg, you may use the Republic's supply causeway."
  7: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0021 [0x24] CREATE_DIALOG(message_id=10836*, default_option=1*, option_flags=0*)
    → "Cross the bridge? [Yes./No.]"
  9: 0x0028 [0x25] WAIT_DIALOG_SELECT()
 10: 0x0029 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00B4
 11: 0x0031 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 12: 0x0033 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 13: 0x0035 [0x46] CAMERA_CONTROL: Disable user control
 14: 0x0037 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 15: 0x0038 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x0049 [0x1C] WAIT(60* ticks)
 17: 0x004C [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 18: 0x004F [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=6.8°*)
 19: 0x0056 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z87a" with entities [LocalPlayer, LocalPlayer], work=[217*, 0*]
 20: 0x0067 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 21: 0x006E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x007F [0x1C] WAIT(60* ticks)
 23: 0x0082 [0x27] REQ_SET(priority=0x01, entity_id=_2f7 (ID: 17134074/0x010571FA), tag_num=0x03)
 24: 0x0089 [0x1C] WAIT(90* ticks)
 25: 0x008C [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x06)
 26: 0x0093 [0x1C] WAIT(180* ticks)
 27: 0x0096 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 28: 0x00A7 [0x1C] WAIT(60* ticks)
 29: 0x00AA [0x03] Work_Zone[1] = 1*
 30: 0x00AF [0x46] CAMERA_CONTROL: Restore default settings
 31: 0x00B1 [0x01] GOTO 0x00C4
 32: 0x00B4 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00C4
 33: 0x00BC [0x03] Work_Zone[1] = 0*
 34: 0x00C1 [0x01] GOTO 0x00C4

SUBROUTINE_00C4:
 35: 0x00C4 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 36: 0x00C6 [0x21] END_EVENT
 37: 0x00C7 [0x00] END_REQSTACK()
```
