# 16859499 - kiokudama_c

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Promyvion - Mea (ID: 20) |
| Block Size       | 132 bytes                |
| Total Events     | 2                        |
| References Count | 4                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [21](#event-21)       | 0x0001       |     90 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0078      |         120 |
|       1 | 0x00C9      |         201 |
|       2 | 0x0000      |           0 |
|       3 | 0x003C      |          60 |

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 90 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 46 01 42 2D F8  FF FF 7F F8 FF FF 7F 73    .F.B-........s
0010: 31 34 32 2D F8 FF FF 7F  F8 FF FF 7F 65 74 30 31  142-........et01
0020: 54 F8 FF FF 7F F8 FF FF  7F 65 74 30 31 1C 00 80  T........et01...
0030: 45 01 80 F0 FF FF 7F F0  FF FF 7F 77 68 6F 31 02  E..........who1.
0040: 80 1C 03 80 45 01 80 F0  FF FF 7F F0 FF FF 7F 77  ....E..........w
0050: 68 69 31 02 80 46 00 20  00 21 00                 hi1..F. .!.     
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x46] CAMERA_CONTROL: Disable user control
  2: 0x0005 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  3: 0x0006 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "s142" with entities [EventEntity, EventEntity]
  4: 0x0013 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "et01" with entities [EventEntity, EventEntity]
  5: 0x0020 [0x54] WAIT_MAP_SCHEDULER: Wait for scheduler "et01" with entities [EventEntity, EventEntity]
  6: 0x002D [0x1C] WAIT(120* ticks)
  7: 0x0030 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  8: 0x0041 [0x1C] WAIT(60* ticks)
  9: 0x0044 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 10: 0x0055 [0x46] CAMERA_CONTROL: Restore default settings
 11: 0x0057 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 12: 0x0059 [0x21] END_EVENT
 13: 0x005A [0x00] END_REQSTACK()
```
