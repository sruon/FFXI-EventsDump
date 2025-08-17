# 17183562 - Torch Stand

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Castle Oztroja [S] (ID: 99) |
| Block Size       | 76 bytes                    |
| Total Events     | 2                           |
| References Count | 3                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [13](#event-13)       | 0x0001       |     39 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1FB7      |        8119 |
|       1 | 0x0000      |           0 |
|       2 | 0x0001      |           1 |

## String References

- **8119**: Light the torch? [Yes./No.]

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

### Event 13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 39 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 24 00 80 01 80  01 80 25 02 00 10 01 80    .$......%.....
0010: 00 1B 00 03 01 10 02 80  01 26 00 02 00 10 02 80  .........&......
0020: 00 26 00 01 26 00 21 00                           .&..&.!.        
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x24] CREATE_DIALOG(message_id=8119*, default_option=0*, option_flags=0*)
    → "Light the torch? [Yes./No.]"
  2: 0x000A [0x25] WAIT_DIALOG_SELECT()
  3: 0x000B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x001B
  4: 0x0013 [0x03] Work_Zone[1] = 1*
  5: 0x0018 [0x01] GOTO 0x0026
  6: 0x001B [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0026
  7: 0x0023 [0x01] GOTO 0x0026

SUBROUTINE_0026:
  8: 0x0026 [0x21] END_EVENT
  9: 0x0027 [0x00] END_REQSTACK()
```
