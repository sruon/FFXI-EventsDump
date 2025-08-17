# 17735736 - Ranpi-Pappi

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Bastok Mines (ID: 234) |
| Block Size       | 128 bytes              |
| Total Events     | 3                      |
| References Count | 7                      |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [77](#event-77)       | 0x0001       |     34 |             10 |
| [78](#event-78)       | 0x0023       |     34 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x29F6      |       10742 |
|       1 | 0x0028      |          40 |
|       2 | 0x29F7      |       10743 |
|       3 | 0x29F8      |       10744 |
|       4 | 0x29F9      |       10745 |
|       5 | 0x29FA      |       10746 |
|       6 | 0x29FB      |       10747 |

## String References

- **10742**: Bastok is a scary-wary place! Open warfare with the Quadav! Everyone fighting!
- **10743**: Windurst is so different! Very peaceful! We bash-mash Yagudo sometimes, yes, but at least we try to talk to them first!
- **10744**: Killing each other isn't the way! My little-brittle bones are shaking!
- **10745**: Bastokers are always grumpy-frumpy because they're fighting all the time!
- **10746**: Honestly speaking, the Galka in this district scare me the most, even more so than the Quadav...
- **10747**: Oopsy-doopsy. That was not a nice thing for me to say! Please don't tell anyone I said that!

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

### Event 77

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 34 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 66 01 80 F8 FF FF   ........#f.....
0010: 7F F8 FF FF 7F 74 6C 6B  30 1D 02 80 23 1D 03 80  .....tlk0...#...
0020: 23 21 00                                          #!.             
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=10742*)
    → "Bastok is a scary-wary place! Open warfare with the Quadav! Everyone fighting!"
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  4: 0x0019 [0x1D] PRINT_EVENT_MESSAGE(message_id=10743*)
    → "Windurst is so different! Very peaceful! We bash-mash Yagudo sometimes, yes, but at least we try to talk to them first!"
  5: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001D [0x1D] PRINT_EVENT_MESSAGE(message_id=10744*)
    → "Killing each other isn't the way! My little-brittle bones are shaking!"
  7: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0021 [0x21] END_EVENT
  9: 0x0022 [0x00] END_REQSTACK()
```

### Event 78

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0023   |
| Data Size    | 34 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          1E F0 FF FF 7F  1D 04 80 23 66 01 80 F8     ........#f...
0030: FF FF 7F F8 FF FF 7F 74  6C 6B 30 1D 05 80 23 1D  .......tlk0...#.
0040: 06 80 23 21 00                                    ..#!.           
```

#### Opcodes

```
  0: 0x0023 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0028 [0x1D] PRINT_EVENT_MESSAGE(message_id=10745*)
    → "Bastokers are always grumpy-frumpy because they're fighting all the time!"
  2: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x002C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  4: 0x003B [0x1D] PRINT_EVENT_MESSAGE(message_id=10746*)
    → "Honestly speaking, the Galka in this district scare me the most, even more so than the Quadav..."
  5: 0x003E [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x003F [0x1D] PRINT_EVENT_MESSAGE(message_id=10747*)
    → "Oopsy-doopsy. That was not a nice thing for me to say! Please don't tell anyone I said that!"
  7: 0x0042 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0043 [0x21] END_EVENT
  9: 0x0044 [0x00] END_REQSTACK()
```
