# 17134060 - Rusted Musket

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Bastok Markets [S] (ID: 87) |
| Block Size       | 80 bytes                    |
| Total Events     | 3                           |
| References Count | 4                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [169](#event-169)     | 0x0001       |     33 |              9 |
| [358](#event-358)     | 0x0022       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0045      |          69 |
|       2 | 0x303C      |       12348 |
|       3 | 0x303D      |       12349 |

## String References

- **12348**: At the battle of Vunkerl Inlet, the Republican Legion's Third Division encountered a gigas raiding party approaching by sea.
- **12349**: The fiends eventually made landfall, but their advance was stopped cold by the brilliant tactics of Legatus Invincible Shield. No doubt his military genius will become the stuff of legend.

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

### Event 169

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 33 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 66 01 80 F8 FF FF 7F   ........f......
0010: F8 FF FF 7F 74 6C 6B 30  1D 02 80 23 1D 03 80 23  ....tlk0...#...#
0020: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(30* ticks)
  2: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=69*
  3: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=12348*)
    → "At the battle of Vunkerl Inlet, the Republican Legion's Third Division encountered a gigas raiding party approaching by sea."
  4: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=12349*)
    → "The fiends eventually made landfall, but their advance was stopped cold by the brilliant tactics of Legatus Invincible Shield. No doubt his military genius will become the stuff of legend."
  6: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0020 [0x21] END_EVENT
  8: 0x0021 [0x00] END_REQSTACK()
```

### Event 358

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0022  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       00                                            .             
```

#### Opcodes

```
  0: 0x0022 [0x00] END_REQSTACK()
```
