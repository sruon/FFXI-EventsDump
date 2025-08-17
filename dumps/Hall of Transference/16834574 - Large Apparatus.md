# 16834574 - Large Apparatus

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Hall of Transference (ID: 14) |
| Block Size       | 408 bytes                     |
| Total Events     | 3                             |
| References Count | 11                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [167](#event-167)     | 0x0001       |    148 |             24 |
| [168](#event-168)     | 0x0095       |    187 |             27 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x003C      |          60 |
|       3 | 0x0013      |          19 |
|       4 | 0x005E      |          94 |
|       5 | 0x1C62      |        7266 |
|       6 | 0x005A      |          90 |
|       7 | 0x00F0      |         240 |
|       8 | 0x00C9      |         201 |
|       9 | 0x0078      |         120 |
|      10 | 0x0001      |           1 |

## String References

- **7266**: You see a honeycomb-like sheet made up of tiny clear hexagonal chips arranged here. One appears to be missing...

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

### Event 167

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 148 bytes |
| Instructions | 24        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 43 00 43 01  46 01 45 00 80 F0 FF FF    .BC.C.F.E.....
0010: 7F F0 FF FF 7F 66 64 6F  31 01 80 1C 02 80 38 03  .....fdo1.....8.
0020: 80 4E 01 F0 FF FF 7F 45  04 80 F8 FF FF 7F F8 FF  .N.....E........
0030: FF 7F 7A 31 34 66 01 80  45 00 80 F0 FF FF 7F F0  ..z14f..E.......
0040: FF FF 7F 66 64 69 31 01  80 1C 02 80 48 05 80 1C  ...fdi1.....H...
0050: 06 80 45 00 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..E..........fdo
0060: 31 01 80 1C 02 80 52 04  80 F8 FF FF 7F F8 FF FF  1.....R.........
0070: 7F 7A 31 34 66 4E 00 F0  FF FF 7F 46 00 1C 02 80  .z14fN.....F....
0080: 45 00 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 31 01  E..........fdi1.
0090: 80 20 00 21 00                                    . .!.           
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  3: 0x0006 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  4: 0x0008 [0x46] CAMERA_CONTROL: Disable user control
  5: 0x000A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  6: 0x001B [0x1C] WAIT(60* ticks)
  7: 0x001E [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  8: 0x0021 [0x4E] SET_ENTITY_HIDE_FLAG: Hide LocalPlayer
  9: 0x0027 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z14f" with entities [EventEntity, EventEntity], work=[94*, 0*]
 10: 0x0038 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 11: 0x0049 [0x1C] WAIT(60* ticks)
 12: 0x004C [0x48] [System] [7266*]:
    → "You see a honeycomb-like sheet made up of tiny clear hexagonal chips arranged here. One appears to be missing..."
 13: 0x004F [0x1C] WAIT(90* ticks)
 14: 0x0052 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 15: 0x0063 [0x1C] WAIT(60* ticks)
 16: 0x0066 [0x52] END_LOAD_SCHEDULER: End scheduler "z14f" with entities [EventEntity, EventEntity], work=94*
 17: 0x0075 [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
 18: 0x007B [0x46] CAMERA_CONTROL: Restore default settings
 19: 0x007D [0x1C] WAIT(60* ticks)
 20: 0x0080 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 21: 0x0091 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 22: 0x0093 [0x21] END_EVENT
 23: 0x0094 [0x00] END_REQSTACK()
```

### Event 168

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0095    |
| Data Size    | 187 bytes |
| Instructions | 27        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                20 01 42  43 00 43 01 46 01 45 00        .BC.C.F.E.
00A0: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 01 80 1C  .........fdo1...
00B0: 02 80 38 03 80 4E 01 F0  FF FF 7F 45 04 80 F8 FF  ..8..N.....E....
00C0: FF 7F F8 FF FF 7F 7A 31  34 67 01 80 45 00 80 F0  ......z14g..E...
00D0: FF FF 7F F0 FF FF 7F 66  64 69 31 01 80 1C 07 80  .......fdi1.....
00E0: 45 08 80 F0 FF FF 7F F0  FF FF 7F 77 68 6F 31 01  E..........who1.
00F0: 80 1C 09 80 03 01 10 0A  80 45 08 80 F0 FF FF 7F  .........E......
0100: F0 FF FF 7F 77 68 69 31  01 80 1C 09 80 45 00 80  ....whi1.....E..
0110: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 01 80 1C 02  ........fdo1....
0120: 80 52 04 80 F8 FF FF 7F  F8 FF FF 7F 7A 31 34 67  .R..........z14g
0130: 4E 00 F0 FF FF 7F 46 00  1C 02 80 45 00 80 F0 FF  N.....F....E....
0140: FF 7F F0 FF FF 7F 66 64  69 31 01 80 20 00 21 00  ......fdi1.. .!.
```

#### Opcodes

```
  0: 0x0095 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0097 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0098 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  3: 0x009A [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  4: 0x009C [0x46] CAMERA_CONTROL: Disable user control
  5: 0x009E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  6: 0x00AF [0x1C] WAIT(60* ticks)
  7: 0x00B2 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  8: 0x00B5 [0x4E] SET_ENTITY_HIDE_FLAG: Hide LocalPlayer
  9: 0x00BB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "z14g" with entities [EventEntity, EventEntity], work=[94*, 0*]
 10: 0x00CC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 11: 0x00DD [0x1C] WAIT(240* ticks)
 12: 0x00E0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 13: 0x00F1 [0x1C] WAIT(120* ticks)
 14: 0x00F4 [0x03] Work_Zone[1] = 1*
 15: 0x00F9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 16: 0x010A [0x1C] WAIT(120* ticks)
 17: 0x010D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x011E [0x1C] WAIT(60* ticks)
 19: 0x0121 [0x52] END_LOAD_SCHEDULER: End scheduler "z14g" with entities [EventEntity, EventEntity], work=94*
 20: 0x0130 [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
 21: 0x0136 [0x46] CAMERA_CONTROL: Restore default settings
 22: 0x0138 [0x1C] WAIT(60* ticks)
 23: 0x013B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 24: 0x014C [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 25: 0x014E [0x21] END_EVENT
 26: 0x014F [0x00] END_REQSTACK()
```
