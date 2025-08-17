# 17428991 - Stone Picture Frame

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Temple of Uggalepih (ID: 159) |
| Block Size       | 116 bytes                     |
| Total Events     | 2                             |
| References Count | 7                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [60](#event-60)       | 0x0001       |     61 |             15 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x1CC3      |        7363 |
|       2 | 0x012C      |         300 |
|       3 | 0x1CC5      |        7365 |
|       4 | 0x00C9      |         201 |
|       5 | 0x0000      |           0 |
|       6 | 0x003C      |          60 |

## String References

- **7363**: Brush in hand, you stand up straight in front of the blank canvas and begin to concentrate.
- **7365**: By focusing your thoughts on the $3, a new painting begins to appear on the canvas...

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

### Event 60

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 61 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 38 00 80 48 01  80 1C 02 80 48 03 80 23    .8..H.....H..#
0010: 43 00 43 01 42 45 04 80  F0 FF FF 7F F0 FF FF 7F  C.C.BE..........
0020: 77 68 6F 31 05 80 1C 06  80 45 04 80 F0 FF FF 7F  who1.....E......
0030: F0 FF FF 7F 77 68 69 31  05 80 20 00 21 00        ....whi1.. .!.  
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x38] SET_CLIENT_EVENT_MODE(mode=1*)
  2: 0x0006 [0x48] [System] [7363*]:
    → "Brush in hand, you stand up straight in front of the blank canvas and begin to concentrate."
  3: 0x0009 [0x1C] WAIT(300* ticks)
  4: 0x000C [0x48] [System] [7365*]:
    → "By focusing your thoughts on the $3, a new painting begins to appear on the canvas..."
  5: 0x000F [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0010 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  7: 0x0012 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  8: 0x0014 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  9: 0x0015 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 10: 0x0026 [0x1C] WAIT(60* ticks)
 11: 0x0029 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 12: 0x003A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 13: 0x003C [0x21] END_EVENT
 14: 0x003D [0x00] END_REQSTACK()
```
