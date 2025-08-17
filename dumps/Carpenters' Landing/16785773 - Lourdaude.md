# 16785773 - Lourdaude

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Carpenters' Landing (ID: 2) |
| Block Size       | 172 bytes                   |
| Total Events     | 6                           |
| References Count | 7                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [26](#event-26)       | 0x0001       |      8 |              5 |
| [24](#event-24)       | 0x0009       |      8 |              5 |
| [22](#event-22)       | 0x0011       |     16 |              9 |
| [25](#event-25)       | 0x0021       |     70 |             13 |
| [27](#event-27)       | 0x0067       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D0D      |        7437 |
|       1 | 0x1D0B      |        7435 |
|       2 | 0x00C8      |         200 |
|       3 | 0x0000      |           0 |
|       4 | 0x0078      |         120 |
|       5 | 0x1D0C      |        7436 |
|       6 | 0x00C9      |         201 |

## String References

- **7435**: <Sniff...sniff...> $2...gil...
- **7436**: ...Done...
- **7437**: ...

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

### Event 26

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 8 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1D 00 80 23 20 00 21  00                        ...# .!.       
```

#### Opcodes

```
  0: 0x0001 [0x1D] PRINT_EVENT_MESSAGE(message_id=7437*)
    → "..."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  3: 0x0007 [0x21] END_EVENT
  4: 0x0008 [0x00] END_REQSTACK()
```

### Event 24

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0009  |
| Data Size    | 8 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                             1D 01 80 23 20 00 21           ...# .!
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0009 [0x1D] PRINT_EVENT_MESSAGE(message_id=7435*)
    → "<Sniff...sniff...> $2...gil..."
  1: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x000D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  3: 0x000F [0x21] END_EVENT
  4: 0x0010 [0x00] END_REQSTACK()
```

### Event 22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 16 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    42 1E F0 FF FF 7F 6F  70 1D 01 80 23 20 00 21   B.....op...# .!
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0011 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0012 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0017 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0018 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0019 [0x1D] PRINT_EVENT_MESSAGE(message_id=7435*)
    → "<Sniff...sniff...> $2...gil..."
  5: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  7: 0x001F [0x21] END_EVENT
  8: 0x0020 [0x00] END_REQSTACK()
```

### Event 25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 70 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    42 1E F0 FF FF 7F 6F  70 45 02 80 F0 FF FF 7F   B.....opE......
0030: F0 FF FF 7F 66 64 6F 31  03 80 1C 04 80 45 02 80  ....fdo1.....E..
0040: F0 FF FF 7F F0 FF FF 7F  66 64 69 31 03 80 1D 05  ........fdi1....
0050: 80 23 45 06 80 F0 FF FF  7F F0 FF FF 7F 71 73 74  .#E..........qst
0060: 63 03 80 20 00 21 00                              c.. .!.         
```

#### Opcodes

```
  0: 0x0021 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0022 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0027 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0028 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0029 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  5: 0x003A [0x1C] WAIT(120* ticks)
  6: 0x003D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  7: 0x004E [0x1D] PRINT_EVENT_MESSAGE(message_id=7436*)
    → "...Done..."
  8: 0x0051 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0052 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 10: 0x0063 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 11: 0x0065 [0x21] END_EVENT
 12: 0x0066 [0x00] END_REQSTACK()
```

### Event 27

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0067  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      00                                  .        
```

#### Opcodes

```
  0: 0x0067 [0x00] END_REQSTACK()
```
