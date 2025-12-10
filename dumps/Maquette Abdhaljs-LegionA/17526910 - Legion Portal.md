# 17526910 - Legion Portal

## Common Data

| Field            | Value                               |
|------------------|-------------------------------------|
| Zone             | Maquette Abdhaljs-LegionA (ID: 183) |
| Block Size       | 80 bytes                            |
| Total Events     | 2                                   |
| References Count | 3                                   |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [10002](#event-10002) | 0x0001       |     43 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1B9F      |        7071 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |

## String References

- **7071**: Proceed to the Hall of [An/Ki/Im/Muru/Mul]? [Yes./Not yet.]

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

### Event 10002

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 43 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 03 0E 00 02 10 24  00 80 01 80 02 80 25 02   B.....$......%.
0010: 00 10 02 80 00 1F 00 03  01 10 01 80 01 2A 00 02  .............*..
0020: 00 10 01 80 00 2A 00 01  2A 00 21 00              .....*..*.!.    
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x03] ExtData[1]->WorkLocal[14] = Work_Zone[2]
  2: 0x0007 [0x24] CREATE_DIALOG(message_id=7071*, default_option=1*, option_flags=0*)
    → "Proceed to the Hall of [An/Ki/Im/Muru/Mul]? [Yes./Not yet.]"
  3: 0x000E [0x25] WAIT_DIALOG_SELECT()
  4: 0x000F [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x001F
  5: 0x0017 [0x03] Work_Zone[1] = 1*
  6: 0x001C [0x01] GOTO 0x002A
  7: 0x001F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x002A
  8: 0x0027 [0x01] GOTO 0x002A

SUBROUTINE_002A:
  9: 0x002A [0x21] END_EVENT
 10: 0x002B [0x00] END_REQSTACK()
```
