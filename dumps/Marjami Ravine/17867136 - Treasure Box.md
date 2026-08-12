# 17867136 - Treasure Box

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Marjami Ravine (ID: 266) |
| Block Size       | 212 bytes                |
| Total Events     | 3                        |
| References Count | 7                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [5006](#event-5006)   | 0x0001       |     24 |              8 |
| [5504](#event-5504)   | 0x0019       |    128 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x0001      |           1 |
|       3 | 0x005A      |          90 |
|       4 | 0x00C9      |         201 |
|       5 | 0x002D      |          45 |
|       6 | 0x000F      |          15 |

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

### Event 5006

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 24 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 2C F8 FF FF  7F F8 FF FF 7F 6F 70 65    .B,........ope
0010: 6E 1C 00 80 2E 20 00 21  00                       n.... .!.       
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "open" with entities [EventEntity, EventEntity]
  3: 0x0011 [0x1C] WAIT(200* ticks)
  4: 0x0014 [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
  5: 0x0015 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  6: 0x0017 [0x21] END_EVENT
  7: 0x0018 [0x00] END_REQSTACK()
```

### Event 5504

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0019    |
| Data Size    | 128 bytes |
| Instructions | 14        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             42 45 00 80 F0 FF FF           BE.....
0020: 7F F0 FF FF 7F 66 64 6F  31 01 80 62 02 80 F0 FF  .....fdo1..b....
0030: FF 7F F0 FF FF 7F 6D 61  69 6E 01 80 1C 03 80 45  ......main.....E
0040: 04 80 F0 FF FF 7F F0 FF  FF 7F 77 68 6F 31 01 80  ..........who1..
0050: 55 04 80 F0 FF FF 7F F0  FF FF 7F 77 68 6F 31 1C  U..........who1.
0060: 05 80 45 00 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..E..........fdo
0070: 31 01 80 55 00 80 F0 FF  FF 7F F0 FF FF 7F 66 64  1..U..........fd
0080: 6F 31 45 04 80 F0 FF FF  7F F0 FF FF 7F 77 68 69  o1E..........whi
0090: 31 01 80 1C 06 80 30 21  00                       1.....0!.       
```

#### Opcodes

```
  0: 0x0019 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x001A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  2: 0x002B [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
  3: 0x003C [0x1C] WAIT(90* ticks)
  4: 0x003F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  5: 0x0050 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=201*
  6: 0x005F [0x1C] WAIT(45* ticks)
  7: 0x0062 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x0073 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  9: 0x0082 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 10: 0x0093 [0x1C] WAIT(15* ticks)
 11: 0x0096 [0x30] SET_UCOFF_CONTINUE_ZERO()
 12: 0x0097 [0x21] END_EVENT
 13: 0x0098 [0x00] END_REQSTACK()
```
