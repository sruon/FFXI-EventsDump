# 17888212 - Living Cairn

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Cirdas Caverns [U] (ID: 271) |
| Block Size       | 120 bytes                    |
| Total Events     | 3                            |
| References Count | 4                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [2016](#event-2016)   | 0x0001       |     42 |             10 |
| [2017](#event-2017)   | 0x002B       |     31 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CFE      |        7422 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |
|       3 | 0x1CFF      |        7423 |

## String References

- **7422**: Teleport to the next location? [Proceed./Not yet.]
- **7423**: Teleport to which area? [None./1."."./4./5./6./7./8./9./10.]

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

### Event 2016

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 42 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    24 00 80 01 80 02 80  25 02 00 10 02 80 00 19   $......%.......
0010: 00 03 01 10 01 80 01 29  00 02 00 10 01 80 00 29  .......).......)
0020: 00 03 01 10 02 80 01 29  00 21 00                 .......).!.     
```

#### Opcodes

```
  0: 0x0001 [0x24] CREATE_DIALOG(message_id=7422*, default_option=1*, option_flags=0*)
    → "Teleport to the next location? [Proceed./Not yet.]"
  1: 0x0008 [0x25] WAIT_DIALOG_SELECT()
  2: 0x0009 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0019
  3: 0x0011 [0x03] Work_Zone[1] = 1*
  4: 0x0016 [0x01] GOTO 0x0029
  5: 0x0019 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0029
  6: 0x0021 [0x03] Work_Zone[1] = 0*
  7: 0x0026 [0x01] GOTO 0x0029

SUBROUTINE_0029:
  8: 0x0029 [0x21] END_EVENT
  9: 0x002A [0x00] END_REQSTACK()
```

### Event 2017

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 31 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   24 03 80 02 80             $....
0030: 02 80 25 02 00 10 02 80  00 43 00 03 01 10 02 80  ..%......C......
0040: 01 43 00 03 01 10 00 10  21 00                    .C......!.      
```

#### Opcodes

```
  0: 0x002B [0x24] CREATE_DIALOG(message_id=7423*, default_option=0*, option_flags=0*)
    → "Teleport to which area? [None./1."."./4./5./6./7./8./9./10.]"
  1: 0x0032 [0x25] WAIT_DIALOG_SELECT()
  2: 0x0033 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0043
  3: 0x003B [0x03] Work_Zone[1] = 0*
  4: 0x0040 [0x01] GOTO 0x0043

SUBROUTINE_0043:
  5: 0x0043 [0x03] Work_Zone[1] = Work_Zone[0]
  6: 0x0048 [0x21] END_EVENT
  7: 0x0049 [0x00] END_REQSTACK()
```
