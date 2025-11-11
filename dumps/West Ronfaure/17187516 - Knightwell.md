# 17187516 - Knightwell

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | West Ronfaure (ID: 100) |
| Block Size       | 120 bytes               |
| Total Events     | 2                       |
| References Count | 7                       |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [141](#event-141)     | 0x0001       |     64 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x003C      |          60 |
|       3 | 0x048C      |        1164 |
|       4 | 0x1F78      |        8056 |
|       5 | 0x00B4      |         180 |
|       6 | 0x1F79      |        8057 |

## String References

- **8056**: <Player> dipped the $3 in the crisp, cool waters of the Knightwell...
- **8057**: The $3 now shimmers a brilliant shade of red!

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

### Event 141

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 64 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 20 01 45 00 80 F0  FF FF 7F F0 FF FF 7F 66   B .E..........f
0010: 64 6F 31 01 80 1C 02 80  03 02 10 03 80 48 04 80  do1..........H..
0020: 1C 05 80 48 06 80 1C 02  80 45 00 80 F0 FF FF 7F  ...H.....E......
0030: F0 FF FF 7F 66 64 69 31  01 80 1C 02 80 20 00 21  ....fdi1..... .!
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x0004 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x0015 [0x1C] WAIT(60* ticks)
  4: 0x0018 [0x03] Work_Zone[2] = 1164*
  5: 0x001D [0x48] [System] [8056*]:
    → "<Player> dipped the $3 in the crisp, cool waters of the Knightwell..."
  6: 0x0020 [0x1C] WAIT(180* ticks)
  7: 0x0023 [0x48] [System] [8057*]:
    → "The $3 now shimmers a brilliant shade of red!"
  8: 0x0026 [0x1C] WAIT(60* ticks)
  9: 0x0029 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x003A [0x1C] WAIT(60* ticks)
 11: 0x003D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 12: 0x003F [0x21] END_EVENT
 13: 0x0040 [0x00] END_REQSTACK()
```
