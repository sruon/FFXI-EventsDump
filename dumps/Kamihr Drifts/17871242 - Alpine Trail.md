# 17871242 - Alpine Trail

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Kamihr Drifts (ID: 267) |
| Block Size       | 148 bytes               |
| Total Events     | 10                      |
| References Count | 6                       |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [44](#event-44)       | 0x0001       |     67 |             22 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1F75      |        8053 |
|       1 | 0x1EE4      |        7908 |
|       2 | 0x0000      |           0 |
|       3 | 0x0001      |           1 |
|       4 | 0x000F      |          15 |
|       5 | 0x0002      |           2 |

## String References

- **7908**: Proceed? [Yes./No.]
- **8053**: This path seems to lead toward the summit of Mount Kamihr.

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

### Event 44

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 67 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 48 00 80 23 24  01 80 02 80 02 80 25 02    .H..#$......%.
0010: 00 10 02 80 00 30 00 03  01 10 03 80 43 00 43 01  .....0......C.C.
0020: 1C 04 80 AB 11 02 80 1C  03 80 30 21 00 01 40 00  ..........0!..@.
0030: 02 00 10 03 80 00 40 00  03 01 10 05 80 01 40 00  ......@.......@.
0040: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x48] [System] [8053*]:
    → "This path seems to lead toward the summit of Mount Kamihr."
  2: 0x0006 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0007 [0x24] CREATE_DIALOG(message_id=7908*, default_option=0*, option_flags=0*)
    → "Proceed? [Yes./No.]"
  4: 0x000E [0x25] WAIT_DIALOG_SELECT()
  5: 0x000F [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0030
  6: 0x0017 [0x03] Work_Zone[1] = 1*
  7: 0x001C [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  8: 0x001E [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  9: 0x0020 [0x1C] WAIT(15* ticks)
 10: 0x0023 [0xAB] EventEntity->DespawnValue = 0* // Set despawn value
 11: 0x0027 [0x1C] WAIT(1* ticks)
 12: 0x002A [0x30] SET_UCOFF_CONTINUE_ZERO()
 13: 0x002B [0x21] END_EVENT
 14: 0x002C [0x00] END_REQSTACK()

SUBROUTINE_0040:
 15: 0x0040 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 16: 0x0042 [0x21] END_EVENT
 17: 0x0043 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x002D [0x01] GOTO 0x0040
```
