# 17613249 - Underground Pool

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Fei'Yin (ID: 204) |
| Block Size       | 192 bytes         |
| Total Events     | 2                 |
| References Count | 6                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [21](#event-21)       | 0x0001       |    143 |             20 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0003      |           3 |
|       2 | 0x0000      |           0 |
|       3 | 0x003C      |          60 |
|       4 | 0x00E7      |         231 |
|       5 | 0x1CE1      |        7393 |

## String References

- **7393**: You throw in $6 and give a moment of silence for the spirits of the beasts.

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

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 143 bytes |
| Instructions | 20        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 4A F0 FF FF  7F F8 FF FF 7F 6F 76 F0    .BJ........ov.
0010: FF FF 7F 2C F0 FF FF 7F  F0 FF FF 7F 73 68 69 74  ...,........shit
0020: 53 F0 FF FF 7F F0 FF FF  7F 73 68 69 74 1C 00 80  S........shit...
0030: 62 01 80 F8 FF FF 7F F8  FF FF 7F 6D 61 69 6E 02  b..........main.
0040: 80 53 F8 FF FF 7F F8 FF  FF 7F 6D 61 69 6E 1C 03  .S........main..
0050: 80 2C F0 FF FF 7F F0 FF  FF 7F 72 65 73 30 53 F0  .,........res0S.
0060: FF FF 7F F0 FF FF 7F 72  65 73 30 03 02 10 04 80  .......res0.....
0070: 48 05 80 23 2C F0 FF FF  7F F0 FF FF 7F 72 65 73  H..#,........res
0080: 32 53 F0 FF FF 7F F0 FF  FF 7F 72 65 73 32 21 00  2S........res2!.
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x4A] LocalPlayer looks at EventEntity
  3: 0x000D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x000E [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
  5: 0x0013 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "shit" with entities [LocalPlayer, LocalPlayer]
  6: 0x0020 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "shit" with entities [LocalPlayer, LocalPlayer]
  7: 0x002D [0x1C] WAIT(30* ticks)
  8: 0x0030 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [EventEntity, EventEntity], work=[3*, 0*]
  9: 0x0041 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "main" with entities [EventEntity, EventEntity]
 10: 0x004E [0x1C] WAIT(60* ticks)
 11: 0x0051 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "res0" with entities [LocalPlayer, LocalPlayer]
 12: 0x005E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "res0" with entities [LocalPlayer, LocalPlayer]
 13: 0x006B [0x03] Work_Zone[2] = 231*
 14: 0x0070 [0x48] [System] [7393*]:
    → "You throw in $6 and give a moment of silence for the spirits of the beasts."
 15: 0x0073 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0074 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "res2" with entities [LocalPlayer, LocalPlayer]
 17: 0x0081 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "res2" with entities [LocalPlayer, LocalPlayer]
 18: 0x008E [0x21] END_EVENT
 19: 0x008F [0x00] END_REQSTACK()
```
